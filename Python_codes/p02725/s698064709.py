n,m=map(int,input().split())
a = list(map(int,input().split()))
a.append(a[0]+n)
ma = -1
for i in range(0, m):
    ma = max(ma, a[i+1]-a[i])
print(n-ma)