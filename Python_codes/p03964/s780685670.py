n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]

taka = l[0][0]
ao = l[0][1]

for i in range(1,n):
    rt = (taka+l[i][0]-1) // l[i][0]
    ra = (ao+l[i][1]-1) // l[i][1]
    r = max(rt,ra)
    taka = r * l[i][0]
    ao = r * l[i][1]

print(taka+ao)
