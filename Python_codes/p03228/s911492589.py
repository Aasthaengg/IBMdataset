a,b,k = map(int, input().split())
for i in range(k):
    if i % 2 == 0: 
        if a % 2 == 0:
            a //= 2
            b += a
        else:
            a -= 1
            a //= 2
            b += a
    else:
        if b % 2 == 0:
            b //= 2
            a += b
        else:
            b -= 1
            b //= 2
            a += b
print(a,b)