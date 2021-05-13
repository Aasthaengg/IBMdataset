N,M=map(int,input().split())
xyz=[list(map(int,input().split())) for _ in range(N)]

MAX=0

for bit in range(2**3):
    sign=[]
    SUM=[]

    for g in range(3):
        if (bit>>g)&1:
            sign.append(1)
        else:
            sign.append(-1)
    
    for g in range(N):
        SUM.append(sign[0]*xyz[g][0]+sign[1]*xyz[g][1]+sign[2]*xyz[g][2])

    SUM.sort(reverse=True)
    MAX=max(MAX,sum(SUM[:M]))

print(MAX)