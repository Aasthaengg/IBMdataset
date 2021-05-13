from bisect import bisect_right
from bisect import bisect_left

icase=0
if icase==0:
    n=int(input())
    a=list(map(int,input().split()))
elif icase==1:
    n=4
    a=[2,5,4,6]
elif icase==2:
    n=9
    a=[0,0,0,0,0,0,0,0,0]
elif icase==3:
    n=19
    a=[885,8,1,128,83,32,256,206,639,16,4,128,689,32,8,64,885,969,1]

amax=max(a)
k=len(bin(amax))-2

cc=[[0]*k for i in range(n)]
for i in range(n):
    ai=bin(a[i])[2:]
#    print(ai)
    kd=k-len(ai)
    for j in range(len(ai)):
        cc[i][kd+j]=int(ai[j])
#print(cc)    
cc2=[[0]*(n+1) for i in range(k)]
for i in range(n):
    for j in range(k):
        cc2[j][i+1]=cc2[j][i]+cc[i][j]
#print(cc2)

icnt=0
for i in range(n):
#    print(i,"-------------")
    cmin=n+1
    for j in range(k):
#    ileft=bisect_left(cc2[j],cc2[j][i]+1,i)
        iright=bisect_right(cc2[j],cc2[j][i]+1,i+1)-(i+1)
        cmin=min(cmin,iright)
#        print(cc2[j])
#        print("j:",j,"v:",cc2[j][i]+1,"i:",i,"ir:",iright,"cmin:",cmin)
    icnt+=cmin
print(icnt)