N=int(input())
A=list(map(int,input().split()))
ave=sum(A)/N
ABS=abs(A[0]-ave)
ans=0
for i,a in enumerate(A):
    if ABS>abs(ave-a):
        ABS=abs(ave-a)
        ans=i
print(ans)
