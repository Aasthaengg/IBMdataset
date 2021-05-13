a,b,c,d = map(int,input().split())
l = a*b
r = c*d
print(l if l > r else r)