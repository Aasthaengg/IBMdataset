def main():
  H,W,K = map(int,input().split())
  S = [[] for _ in range(H)]
  for i in range(H):
    for s in input():
      S[i].append(int(s))
  #print(S)
  
  ans = 10000
  for i in range(2**(H-1)):
    # 横方向の割り方を全検索する。
    # T:横方向の割り方を固定したときに、同じブロック内のホワイトチョコの個数を縦方向に集約した配列。
    th = bin(i).count('1')
    T = [[0 for _ in range(W)] for _ in range(th+1)]
    ti = 0
    for j in range(H):
      for k in range(W):
        T[ti][k] += S[j][k]
      if (i>>j)&1 == 1:
        ti += 1
    #print(th,T)

    # 縦方向の1列分の中に、Kより大きい個数のホワイトチョコが含まれる場合は
    # どのように割っても条件を満たさないのでスキップする。
    f = True
    for k in range(W):
      for j in range(th+1):
        if T[j][k] > K:
          f = False
    if not f:
      continue

    # 横方向に順にホワイトチョコの数を数えていき、Kを超える場合は割る回数ans0を+1する。
    ans0 = th
    T0 = [0 for _ in range(th+1)]
    for k in range(W):
      f = True
      for j in range(th+1):
        T0[j] += T[j][k]
        if T0[j] > K:
          f = False
      if not f:
        ans0 += 1
        # 割った場合は、カウントしていたホワイトチョコの数をカレントの1列分に戻す。
        for j in range(th+1):
          T0[j] = T[j][k]
    ans = min(ans0,ans)
  print(ans)

main()