n, a, b = map(int, input().split())
if a > b: print(0)
elif a == b:
    print(n*(b-a)+1)
else:
    if n == 1 : print(0)
    else: print((n-1)*b+a - ((n-1)*a+b)+1)