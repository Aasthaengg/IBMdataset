n=int(input())
A=tuple(map(int,input().split()))
ave=sum(A)/n
d=float('inf')
for i,a in enumerate(A):
    if abs(a-ave)<d:
        d=abs(a-ave)
        ans=i
print(ans)