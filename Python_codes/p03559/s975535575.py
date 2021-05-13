from bisect import bisect_right,bisect_left
n=int(input())
a=sorted(list(map(int,input().split())))
b=list(map(int,input().split()))
c=sorted(list(map(int,input().split())))
ans=0
for i in b:ans+=bisect_left(a,i)*(n-bisect_right(c,i))
print(ans)