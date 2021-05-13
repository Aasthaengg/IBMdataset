n,k = map(int, input().split())
p = list(map(int, input().split()))

kitai = [(1+p[i])/2 for i in range(n)]

total = sum(kitai[i] for i in range(k))
ans = total

for i in range(0, n-k):
  total = total - kitai[i] + kitai[i+k]
  if total > ans:
    ans = total

print(ans)