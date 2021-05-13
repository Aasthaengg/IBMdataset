n = int(input())
XL = []
for i in range(n):
  x, l = map(int, input().split())
  XL.append([x, l])
  
XL.sort(key=lambda x: x[0]+x[1])

seen = -10**10
ans = 0
for i in range(n):
  rob = XL[i]
  if seen <= rob[0]-rob[1]:
    seen = rob[0]+rob[1]
    ans += 1

print(ans)