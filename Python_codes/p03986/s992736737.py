def agc005_a():
  x = str(input())
  s_accum = [0]
  t_accum = [0]
  t_up = 0
  for ch in x:
    # SとTの出現回数の累積和
    if ch == 'S':
      s_accum.append(s_accum[-1] + 1)
      t_accum.append(t_accum[-1])
    else:
      s_accum.append(s_accum[-1])
      t_accum.append(t_accum[-1] + 1)
    # Tの左側にいるSとの差分が、残るTの数で、プラスの値ならTが先頭に残る
    if ch == 'T':
      t_up = max(t_up, t_accum[-1] - s_accum[-1])
  ans = 2 * t_up
  print(ans)

agc005_a()