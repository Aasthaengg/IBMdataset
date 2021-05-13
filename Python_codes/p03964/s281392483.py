ma = lambda : map(int,input().split())
ni = lambda :int(input())

n = ni()
pt,pa = ma()
for i in range(n-1):
    t,a = ma()
    l = max((pt+t-1)//t,(pa+a-1)//a)
    pt = t*l
    pa = a*l
print(pt+pa)
