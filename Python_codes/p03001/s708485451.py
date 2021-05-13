W,H,x,y = map(int,input().split())
if W/2 == x and H/2 == y:
  pat = 1
else:
  pat = 0
ans =W*H/2
ret = [ans, pat]
print(*ret)