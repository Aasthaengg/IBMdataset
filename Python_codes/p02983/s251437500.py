L,R = list(map(int,input().split()))

ans = float("inf")

for i in range(L,min(R,L+2019)):
  for j in range(L+1,min(R,L+2019)+1):
    ans = min(ans, i * j % 2019)
    
print(ans)