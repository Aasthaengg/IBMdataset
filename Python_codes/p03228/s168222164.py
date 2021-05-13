a,b,k = map(int,input().split())

cnt = 0

for i in range(k):
    if cnt%2 == 0:
        if a%2 == 0:
            a = a//2
            b += a
            cnt += 1
        else:
            a -= 1
            a = a//2
            b += a
            cnt += 1
    else:
        if b%2 == 0:
            b = b//2
            a += b
            cnt += 1
        else:
            b -= 1
            b = b//2
            a += b
            cnt += 1

print(a,b) 