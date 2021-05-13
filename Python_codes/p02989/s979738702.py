n=int(input())
d=list(map(int,input().split()))
d.sort()
if d[n//2]!=d[n//2-1]:
    ans=d[n//2]-d[n//2-1]
else:
    ans=0
print(ans)