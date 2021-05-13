N,M=map(int,input().split())

#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合
S = [[0 for j in range(2)] for i in range(M)]

for i in range(M):
    X,L=map(int,input().split())
    S[i][0]=X
    S[i][1]=L


T=sorted(S,key=lambda x:x[1])
#U=sorted(T,key=lambda x:x[1])



count=1
last=T[0][1]
#print(T)
for i in range(1,M):
    if T[i][0]>=last:
        count+=1
        last=T[i][1]
print(count)

