n, m = map(int, input().split())
need = [list(map(int, input().split())) for i in range(m)]
need = sorted(need, key=lambda x: x[1])

ans = 1
stock = need[0][1]
for i in range(m):
  if stock <= need[i][0]:
    ans += 1
    stock = need[i][1]
    
print(ans)