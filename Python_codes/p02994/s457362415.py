n, l = map(int, input().split())

if l > 0:
    print((n-1)*(2*l+n)//2)
elif l+n-1 < 0:
    print((n-1)*(2*l+n-2)//2)
else:
    print(n*(2*l+n-1)//2)
