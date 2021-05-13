a,b,k = map(int,input().split())
for i in range(k):
    if i%2==0:
        if a%2==1:
            a-=1
        c =a//2
        b+=c
        a-=c
    else:
        if b%2==1:
            b-=1
        c =b//2
        a+=c
        b-=c
print(a,b)