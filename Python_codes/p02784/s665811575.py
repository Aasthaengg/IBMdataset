h,n = map(int,input().split())
a = list(map(int, input().split()))
hoge = sum(a)
h -= hoge
if h <= 0:
    print('Yes')
else:
    print('No')