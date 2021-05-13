n=int(input())
minv=int(input())
maxv=-1*float('inf')
for i in range(n-1):
    r=int(input())
    maxv=max(maxv,r-minv)
    minv=min(minv,r)
print(maxv)
