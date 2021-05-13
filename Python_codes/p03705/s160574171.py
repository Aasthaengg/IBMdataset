n,a,b = map(int,input().split())

minimum = a*(n-1) + b
maximum = b*(n-1) + a

ans = maximum-minimum+1

if a > b or (n == 1 and a != b):
    print(0)
else:
    print(ans)
