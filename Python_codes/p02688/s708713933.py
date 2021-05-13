n, k = list(map(int, input().split()))

s = set()
for _ in range(k):
  kk = input()
  a = list(map(int, input().split()))
  for x in a:
    s.add(x)
print(n - len(s))