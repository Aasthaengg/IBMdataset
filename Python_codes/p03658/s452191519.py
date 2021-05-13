N, K = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0

for i in range(K):
  M = max(ls)
  index = ls.index(M)
  ls[index] = 0
  ans+= M
  
print(ans)