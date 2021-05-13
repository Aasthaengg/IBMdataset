a,b,k=map(int,input().split())
cnt=k
while(k>0):
    if a %2==1:
        a-=1
        b+=a//2
        a//=2
        cnt-=1
        # print(a,b,k)
    else:
        b += a // 2
        a//=2
        cnt -= 1

    if cnt==0:
        print(a,b)
        break
    if b %2==1:
            b -= 1
            a += b // 2
            b//=2
            cnt -= 1
            # print(a,b,k)
    else:
        a += b // 2
        b//=2
        cnt -= 1

    if cnt==0:
        print(a,b)
        break
