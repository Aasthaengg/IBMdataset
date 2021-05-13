d,n = map(int, input().split())
if d==0:
    if n!=100:
        print(1*n)
    else:
        print(101)
else:
    if n!=100:
        print(100**d*n)
    else:
        print(100**d*n+100**d)