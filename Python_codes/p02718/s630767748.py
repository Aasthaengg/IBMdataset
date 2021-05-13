n,m =map(int,input().split())
a = list(map(int,input().split()))
a.sort()
if a[n-m] >=sum(a)/(4*m):
    print('Yes')
else:
    print('No')