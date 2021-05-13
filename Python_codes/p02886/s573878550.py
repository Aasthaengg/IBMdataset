N = int(input())
D = list(map(int,input().split()))
ans = 0

for n in range(N-1):
  ans+=sum(D[n]*D[n+1:])
  
print(ans)