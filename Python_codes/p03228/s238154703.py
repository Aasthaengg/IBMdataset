a,b,k=map(int,input().split())

for i in range(1,k+1):
    if i%2:
        if a%2:
            a-=1
        a//=2
        b+=a
    else:
        if b%2:
            b-=1
        b//=2
        a+=b

print(a,b)