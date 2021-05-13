N,M = map(int,input().split())
AB =[list(map(int,input().split())) for i in range(N)]

AB = sorted(AB)
total=0
for i in range(N):
    if AB[i][1]>M:
        total = total + AB[i][0]*M
        break
    else:
        total = total + AB[i][0]*AB[i][1]
        M = M - AB[i][1]

print(total)