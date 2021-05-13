N,C=map(int,input().split())
D=[]
D.append([0 for i in range(C+1)])
for i in range(C):
    d=[0]+list(map(int,input().split()))
    D.append(d)
#print(D)
L=[]
for i in range(N):
    c=list(map(int,input().split()))
    L.append(c)

M0=[0 for i in range(C+1)]
M1=[0 for i in range(C+1)]
M2=[0 for i in range(C+1)]

for i in range(N):
    for j in range(N):
        if (i+j)%3==0:
            M0[L[i][j]]+=1
        elif (i+j)%3==1:
            M1[L[i][j]]+=1
        elif (i+j)%3==2:
            M2[L[i][j]]+=1
#print(M0,M1,M2)

Col=[i for i in range(1,C+1)]
#print(Col)
import itertools
Arr=list(itertools.permutations(Col,3))
#print(Arr)
ans=10**20
for i in range(len(Arr)):
    cnt=0
    for j in range(1,C+1):
        cnt+=M0[j]*D[j][Arr[i][0]]
        cnt+=M1[j]*D[j][Arr[i][1]]
        cnt+=M2[j]*D[j][Arr[i][2]]
    if ans>cnt:
        ans=cnt
    #print(cnt,Arr[i])
print(ans)

