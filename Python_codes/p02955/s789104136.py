import math
n, k = map(int,input().split())
a = list(map(int, input().split()))

asum = sum(a)
gcdmax = int(math.sqrt(asum))
li = []
for i in range(2,gcdmax+1):
    if asum%i==0:
        li.append(i)
for i in range(gcdmax,0,-1):
    if asum%i==0:
        li.append(asum//i)


ans = 1
# print(li)

for i in li:
    b = [a[ii] % i for ii in range(n)]
    b.sort()
#     print(i,b)
    l = 0
    r = 0
    x = 0
    y = n-1
    while x<=y:
        if r>=l:
            l += b[x]
            x += 1
        else:
            r += i - b[y]
            y -= 1
#         print(l,r)
    if max(l,r) <= k and (l-r)%i==0 :
        ans = i

print(ans)