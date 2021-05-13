a,b = map(int,input().split())
c1,c2,mx1,mx2 = (".","#",a,b) if a < b else ("#",".",b,a)
grid = [[c1]*100 for _ in range(100)]
cnt1 = 1
cnt2 = 0   

for i in range(0,100,4):
    for j in range(0,100,4):
        if cnt1 < mx1:
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if k == i+1 and l == j+1: continue
                    grid[k][l] = c2
            cnt1 += 1
            cnt2 += 1
        elif cnt2 < mx2:
            grid[i][j] = c2
            cnt2 += 1
        else:
            break

print(100,100)
for i in range(100): print("".join(grid[i]))