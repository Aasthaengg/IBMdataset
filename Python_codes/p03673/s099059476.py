n=int(input())
a=list(map(int,input().split()))

l=a[0:n:2]
r=a[1:n:2]
if n%2==1:
    print(*l[::-1],*r)
else:
    print(*r[::-1],*l)
