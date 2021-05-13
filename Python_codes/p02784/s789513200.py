h,n = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a)
if h > s:
    print('No')
else:
    print('Yes')