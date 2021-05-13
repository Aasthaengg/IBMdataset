n,m = map(int,input().split())
a = []
for i in range(n):
    r,t = map(int,input().split())
    a.append((t,r))
a.sort(reverse = True)
#print(a)
d = {}
cd = []
dp = 0
x = 0
 
for i in range(m):
    z,c = a[i]
    dp += z
    if c in d:
        cd.append(z)
    else:
        d[c] = z
        x += 1
#print(cd)
cd.sort(reverse = True)
ans = dp + x**2
c = ans
 
for i in range(m,n):
    if len(cd) == 0:
        break
    z,v = a[i]
    if v in d:
        continue
    d[v] = z
    x += 1
    c = c - cd.pop()+z+2*x-1
    if c > ans:
        ans = c
print(ans)