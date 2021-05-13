n,k=map(int,input().split())
h=list(map(int,input().split()))
if n<=k:
    print(0)
else:
    x=sorted(h)[:(n-k)]
    print(sum(x))