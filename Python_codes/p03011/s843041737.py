p,q,r = map(int,input().split())
l = (p+q, p+r, q+p, q+r, r+p, r+q)
print(min(l))