a,b,k = map(int,input().split())

i = 1
while i <=k:
    if i%2 == 1:
        if a%2 == 1:
            a -=1
            a //=2
            b +=a
        else:
            a //=2
            b +=a

    else:
        if b%2 == 1:
            b -=1
            b //=2
            a +=b
        else:
            b //=2
            a +=b

    i +=1

print(a,b)