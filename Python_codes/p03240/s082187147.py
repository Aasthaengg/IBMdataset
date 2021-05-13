n = int(input())
pos=[]
for i in range(n):
  x,y,h = map(int, input().split())
  pos.append([x,y,h])

pos = sorted(pos, key=lambda x: x[2])
tx,ty,th = pos[-1]
def solve():
  for cx in range(101):
    for cy in range(101):
      H = th+abs(tx-cx)+abs(ty-cy)
      for x,y,h in pos:
        if h != max(H-abs(x-cx)-abs(y-cy), 0):
          break
      else:
        return(cx,cy,H)

cx,cy,H=solve()
print(cx,cy,H)