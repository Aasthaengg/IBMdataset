a,b,k=map(int,input().split())
for i in range(1,k+1):
    if (i % 2) == 1:
        if (a % 2) == 1:
            a -= 1
            a //= 2
            b += a
        else:
            a //= 2
            b += a
    else:
        if (b % 2) == 1:
            b -= 1
            b //= 2
            a += b
        else:
            b //= 2
            a += b
print(str(a)+" "+str(b))
