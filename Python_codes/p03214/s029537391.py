n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
ans=0
mini=float('inf')
for x,i in enumerate(a):
    if abs(i-ave)<mini:
        mini=abs(i-ave)
        ans=x
print(ans)