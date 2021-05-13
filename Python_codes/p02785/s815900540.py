n,k=map(int,input().split())
h=sorted(list(map(int, input().split())))
res=0
if k>=n:res=0
else:
    res+=sum(h[:n-k])
print(res)