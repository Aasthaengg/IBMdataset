n = int(input())

if (n-1)%2 == 0:
    print((n*(n-1)//2))
else:
    print(n*(n-2)//2 + n//2)