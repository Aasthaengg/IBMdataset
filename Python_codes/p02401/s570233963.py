while True:
    a,op,b=input().split()
    ans=None
    a = int(a)
    b = int(b)
    if op=='?':
        break
    elif op=="+":
        ans=a+b
    elif op=='-':
        ans=a-b
    elif op=='*':
        ans=a*b
    else:
        ans=a//b
    print(ans)

