n,k = map(int,input().split())
x = tuple(map(int, input().split()))

for i,v in enumerate(x):
    if v == 1:
        r = i
a,b = divmod(r,k-1)
if b > 0:
    a += 1
r = a * (k-1)

l = n-r-1
if l > 0:
    c,d = divmod(l, k-1)
    if d > 0:
        c += 1
    a += c

print(a)