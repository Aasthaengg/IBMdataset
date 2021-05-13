N=int(input())

#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合
S = [[0 for j in range(2)] for i in range(N)]

for i in range(N):
    X,L=map(int,input().split())
    S[i][0]=X-L
    S[i][1]=X+L


T=sorted(S,key=lambda x:x[1])
#U=sorted(T,key=lambda x:x[1])
if N==1:
    print(1)
    exit()


count=1
last=T[0][1]
for i in range(1,N):
    if T[i][0]>=last:
        count+=1
        last=T[i][1]
print(count)

