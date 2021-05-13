def resolve():
    a,b=map(int, input().split())
    ans=0
    if a >= b:
        ans+= a
        a = a-1
        if a >= b:
            ans+= a

        elif b > a:
            ans+= b

    elif b > a:
        ans+= b
        b = b-1
        if a >= b:
            ans+= a

        elif b>a:
            ans+= b
    print(ans)
resolve()