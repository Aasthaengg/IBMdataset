W,H,N=map(int,input().split())
xya=[list(map(int,input().split())) for i in range(N)]

first=[0,0]
last=[W,H]

for i in range(N):
    if first[0]<xya[i][0] and xya[i][2]==1:
        first[0]=xya[i][0]
    if last[0]>xya[i][0] and xya[i][2]==2:
        last[0]=xya[i][0]
    if first[1]<xya[i][1] and xya[i][2]==3:
        first[1]=xya[i][1]
    if last[1]>xya[i][1] and xya[i][2]==4:
        last[1]=xya[i][1]

area=0
if last[0]<=first[0] or last[1]<=first[1]:
    pass
else:
    area=(last[0]-first[0])*(last[1]-first[1])

print(area)
