a,b,k = map(int, input().split())

for _ in range(k//2):
    if a%2: a-=1
    b += a//2
    a -= a//2

    if b%2: b-=1
    a += b//2
    b -= b//2

if k%2:
    if a%2: a-=1
    b += a//2
    a -= a//2
    


print(a,b)
