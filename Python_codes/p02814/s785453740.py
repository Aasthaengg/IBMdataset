import sys
N,M=map(int,input().split())
A=list(set(map(int,input().split())))
N=len(A)
A=[a//2 for a in A]
 
def f(x):
    cnt=0
    while x%2==0:
        x//=2
        cnt+=1
    return cnt
C=f(A[0])
for a in A:
    if f(a)!=C:
        print(0)
        sys.exit()
def lcm(x,y):
    xy=x*y
    while y!=0:
        x,y=y,x%y
    return xy//x
LCM=A[0]
for i in range(1,N):
    LCM=lcm(LCM,A[i])
if LCM>M:
    ans=0
else:
    M//=LCM
    ans=(M+1)//2
print(ans)