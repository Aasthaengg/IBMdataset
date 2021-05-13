N=int(input())
TA=[list(map(int,input().split())) for i in range(N)]
Taka=1
Aoki=1

def UP(V1,V2,R1,R2):
    n=max(-(-V1//R1),-(-V2//R2))
    return(n*R1,n*R2)

for i in range(N):
    up=UP(Taka,Aoki,TA[i][0],TA[i][1])
#    print(up)
    Taka=up[0]
    Aoki=up[1]

print(Taka+Aoki)