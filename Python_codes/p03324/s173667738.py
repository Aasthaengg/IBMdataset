
d, n = map(int,input().split())

if n == 100:
    print(100**d*101)
else:
    print(str(n)+'00'*d)