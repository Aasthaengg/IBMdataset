def resolve():
  N, T = map(int, input().split())
  t = list(map(int, input().split()))
  ans = 0
  till = 0
  for now in t:
    if till > now:
      ans -= till - now
    till = now + T
    ans += T
  print(ans)
  return

if __name__ == "__main__":
  resolve()
