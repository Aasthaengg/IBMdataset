def resolve():
  N, T = map(int, input().split())
  tt = list(map(int, input().split()))
  ans = 0
  last = 0

  for t in tt:
    if t >= last:
      ans += T
      last = t + T
    else:
      ans += t + T - last
      last = t + T

  print(ans)

  return

if __name__ == "__main__":
  resolve()
