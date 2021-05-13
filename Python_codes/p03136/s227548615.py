n=int(input())
L=list(map(int,input().split()))
L.sort()
ans=sum(L)-L[n-1]
if ans>L[n-1]:
    print('Yes')
else:
    print('No')