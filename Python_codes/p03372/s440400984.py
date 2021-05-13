N,C=map(int,input().split())
XV=[list(map(int,input().split())) for i in range(N)]

RIGHTSUM=[0]

for x,v in XV:
    RIGHTSUM.append(RIGHTSUM[-1]+v)

LEFTSUM=[0]

for x,v in XV[::-1]:
    LEFTSUM.append(LEFTSUM[-1]+v)

RIGHT=[]

for i in range(N):
    RIGHT.append(RIGHTSUM[i+1]-XV[i][0])

LEFT=[]

for i in range(N):
    LEFT.append(LEFTSUM[i+1]-(C-XV[-i-1][0]))


RIGHTMAX=[RIGHT[0]]

for i in range(1,N):
    RIGHTMAX.append(max(RIGHTMAX[i-1],RIGHT[i]))

LEFTMAX=[LEFT[0]]

for i in range(1,N):
    LEFTMAX.append(max(LEFTMAX[i-1],LEFT[i]))

ANS=max(max(RIGHT),max(LEFT),0)
#print(ANS)
for i in range(N-1):
    #print(i,RIGHTSUM[i+1]-XV[i][0]*2+LEFTMAX[N-i-2],LEFTSUM[i+1]-(C-XV[-i-1][0])*2+RIGHTMAX[N-i-2])
    if ANS<(RIGHTSUM[i+1]-XV[i][0]*2)+LEFTMAX[N-i-2]:
        ANS=RIGHTSUM[i+1]-XV[i][0]*2+LEFTMAX[N-i-2]
    if ANS<LEFTSUM[i+1]-(C-XV[-i-1][0])*2+RIGHTMAX[N-i-2]:
        ANS=LEFTSUM[i+1]-(C-XV[-i-1][0])*2+RIGHTMAX[N-i-2]

print(ANS)
    
