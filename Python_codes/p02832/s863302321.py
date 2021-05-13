n=int(input())
ar=list(map(int,input().split()))
m=0
for i in ar:
    if i-1==m:
        m=i
if m: print(n-m)
else: print(-1)
