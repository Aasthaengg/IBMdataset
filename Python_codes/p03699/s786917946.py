def main():
  N = int(input())
  S = [int(input()) for _ in range(N)]
  t = sum(S)
  if t % 10 != 0:
    return t
  S.sort()
  for s in S:
    if s % 10 != 0:
      return t - s
  return 0
print(main())