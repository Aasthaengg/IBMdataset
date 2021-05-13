a,b,k=map(int,input().split())
for i in range(k):
    if i%2:
        if b%2:b-=1
        a,b=a+b//2,b//2
    else:
        if a%2:a-=1
        a,b=a//2,b+a//2

print(a,b,sep=' ')