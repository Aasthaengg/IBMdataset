import itertools
n,p = map(int,input().split())
a = list(map(lambda x:int(x)&1,input().split()))
cnt0 = a.count(0)
cnt1 = n - cnt0
if p==0 and cnt0==n:
    print(2**n)
elif p==1 and cnt0==n:
    print(0)
else:
    print(2**(n-1))