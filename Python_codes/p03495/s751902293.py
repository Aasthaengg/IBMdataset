N, K = map(int, input().split())
A = map(int, input().split())
d = {}

for a in A:
  if a in d:
    d[a] += 1
  else:
    d[a] = 1

num = list(d.values())
num.sort(reverse=True)
print(sum(num[K:]))