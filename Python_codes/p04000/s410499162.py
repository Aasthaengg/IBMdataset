from collections import defaultdict

H, W, N = map(int,input().split())
  
ans =[(H-2)*(W-2)]+[0]*9
blacks = defaultdict(int)
for i in range(N):
  a, b = map(int,input().split())
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      if 2 <= a+dx <H and 2 <= b+dy <W:
        ans[blacks[(a+dx,b+dy)]]-=1
        ans[blacks[(a+dx,b+dy)]+1]+=1
      blacks[(a+dx,b+dy)]+=1
        
for i in range(10): print(ans[i])
