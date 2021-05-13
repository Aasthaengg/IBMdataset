W,H,x,y = map(int, input().split())

quad = [[0,0],[W,0],[W,H],[0,H]] 
S = (quad[1][0]-quad[0][1]) * (quad[2][1]-quad[0][1])
ans = 0

if W/2 == x and H/2 == y:
    ans = 1

print(S/2 , ans)
