N = int(input())
A = list(map(int, input().split()))
lis = [0]*(N+1)
for i in range(N,0,-1):
  k = i*2
  cnt = 0
  while k<=N:
    cnt ^= lis[k]
    k += i
  lis[i] = cnt^A[i-1]
print(lis.count(1))
ans = []
for i in range(1,N+1):
  if lis[i]==1:
    ans.append(i)
if len(ans):
  print(*ans)