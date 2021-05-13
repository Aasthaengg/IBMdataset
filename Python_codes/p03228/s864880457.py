a,b,k = map(int,input().split())
c = 0
for i in range(k):
    a = int(a//2)
    b += a
    c += 1
    if c==k: print(a,b)
    b = int(b//2)
    a += b
    c += 1
    if c==k: print(a,b)