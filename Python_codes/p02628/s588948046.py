n, k= map(int, input().split())
p = list(map(int, input().split()))
p.sort()
S = 0
for i in range(k):
  S = S + p[i]
print(S)