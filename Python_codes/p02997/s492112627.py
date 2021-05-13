n,k = map(int,input().split())

if k > (n-1)*(n-2)//2:
    print(-1)
    exit()

b = (n-1)*(n-2)//2-k

print(b+n-1)
for i in range(n-1):
    print(1,i+2)

a = 2
d = 3
for i in range(b):
    print(a,d)
    if d == n:
        a += 1
        d = a+1
    else:
        d += 1