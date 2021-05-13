
a,b,k = map(int,input().split())

for i in range(k):
    if i%2==0:
        if a%2==1:
            a=max(a-1,0)
        b+=(a//2)
        a//=2
    else:
        if b%2==1:
            b=max(b-1,0)
        a+=(b//2)
        b//=2
print(a,b)
