d, n = list(map(int,input().split()))
if n != 100:
    print((100**d)*n)
else:
    print(101*(100**d))