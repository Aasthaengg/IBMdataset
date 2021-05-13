N = int(input())

lst = []
for _ in range(N):
  x, d = map(int, input().split())
  l = x - d
  r = x + d
  lst.append([l,r])
  
lst.sort(key=lambda x:x[1])

ans = 0
t = lst[0][0]-1
for i in range(N):
  if t <= lst[i][0]:
    ans += 1
    t = lst[i][1]
    
print(ans)