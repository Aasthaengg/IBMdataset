n,m,x = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
s=0
t=0
for i in range(m):
    if a[i]<x:
        s=s+1
    else:
        t=t+1
print(min(s,t))