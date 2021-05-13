a,b,k=map(int,input().split())
i=0
while i<k:
    if i%2==0:
        b+=a//2
        a=a//2
    else:
        a+=b//2
        b=b//2
    i+=1
print(a,b)