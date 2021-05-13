p,q,r = map(int, input().split())

l=[0,0,0]
l[0]=p+q
l[1]=p+r
l[2]=q+r
print(min(l))
