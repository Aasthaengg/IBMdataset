n=int(input())
if n%2: print(0)
else:
    s=0
    x=10
    while n//x:
        s+=n//x
        x*=5
    print(s)
