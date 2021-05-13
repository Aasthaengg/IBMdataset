import bisect
n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))
d=0
for t in b:
    d+=bisect.bisect_left(a,t)*(n-bisect.bisect_right(c,t))
print(d)