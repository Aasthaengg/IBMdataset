def digitsum(s):
  s = str(s)
  a = 0
  for i in range(len(s)):
    a += int(s[i])
  return a

N, A, B = list(map(lambda x: int(x), input().split(" ")))

print(sum([j for j in range(N + 1) if A <= digitsum(j) <= B]))