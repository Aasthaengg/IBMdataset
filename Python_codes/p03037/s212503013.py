N,M = map(int,input().split())
right = N
left = 1
for _ in range(M):
  a,b = map(int,input().split())
  right = min(right,b) 
  left = max(left,a)

ans = right-left+1
print(max(0,ans))