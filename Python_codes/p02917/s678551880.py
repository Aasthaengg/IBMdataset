n,*b=map(int,open(0).read().split())
a=[0]*n
a[0]=b[0]
a[-1]=b[-1]
for i in range(n-2):
    if b[i+1]>=b[i]:
        a[i+1]=b[i]
    else:
        a[i+1]=b[i+1]
print(sum(a))