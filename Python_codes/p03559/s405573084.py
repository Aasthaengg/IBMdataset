import bisect
n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))
cnt=0
for x in b:
     a_=bisect.bisect_left(a,x)
     c_=n-bisect.bisect_right(c,x)
     cnt+=a_*c_
print(cnt)