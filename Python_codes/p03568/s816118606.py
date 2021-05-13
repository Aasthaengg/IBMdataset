import itertools
N=int(input())
A=list(map(int,input().split()))
lo=[-1,0,1]
cnt=0
for k in itertools.product(lo,repeat=N):
    li=list(k)
    res=1
    for z in range(N):
        res*=A[z]+li[z]
    if(res%2==0):
        cnt+=1
print(cnt)