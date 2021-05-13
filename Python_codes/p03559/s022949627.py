from bisect import bisect_left, bisect
n=int(input())
la=sorted(list(map(int,input().split())))
lb=list(map(int,input().split()))
lc=sorted(list(map(int,input().split())))
ans=0
for i in lb:
    ans+=bisect_left(la,i)*(len(lc)-bisect(lc,i))
print(ans)