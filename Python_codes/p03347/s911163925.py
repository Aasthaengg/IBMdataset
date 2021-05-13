import sys
input=sys.stdin.readline
n=int(input())
A=[int(input()) for _ in range(n)]
if A[0]!=0:
    print(-1)
    exit()
for i in range(n-1):
    if A[i]+1<A[i+1]:
        print(-1)
        exit()
ans=0
prev=A[0]
for i,a in enumerate(A,1):
    if a==prev+1:
        ans+=1
    else:
        ans+=a
    prev=a
print(ans)