a,b,k = map(int,input().split())
cnt=0
while cnt < k:
    if cnt%2==0:
        if a%2==0:
            b+=a//2
            a=a//2
            cnt+=1
        else:
            a-=1
            cnt+=1
            b+=a//2
            a=a//2
    else:
        if b%2==0:
            a+=b//2
            b=b//2
            cnt+=1
        else:
            b-=1
            cnt+=1
            a+=b//2
            b=b//2
print(a,b)

