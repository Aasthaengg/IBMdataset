n=int(input())
if n==0:
    print(0)
else:
    ans=""
    while n!=0:
        if n&1:
            n-=1
            ans='1'+ans
        else:
            ans='0'+ans
        n//=-2
    print(ans)
