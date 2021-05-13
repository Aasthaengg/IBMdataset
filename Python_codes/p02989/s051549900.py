n=int(input())
d=list(map(int,input().split()))
d.sort()
k=int(n/2)-1
if d[k]==d[k+1]:
    print(0)
else:
    print(d[k+1]-d[k])