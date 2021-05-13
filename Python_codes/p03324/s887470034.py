n, k = map(int, input().split())
if k == 100:
    print(101*(100**n))
else:
    print((100**n)*k)
