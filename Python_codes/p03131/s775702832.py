k,a,b = map(int,input().split())
if a+1 >= b:
    print(1+k)
else:
    if k // (a+1) == 0:
        print(1+k)
    else:
        k -= a+1
        ans = b
        if k%2 == 0:
            print(ans+k//2*(b-a))
        else:
            print(ans+k//2*(b-a)+1)
