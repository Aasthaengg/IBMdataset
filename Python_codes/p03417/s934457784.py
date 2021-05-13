n, m = map(int, input().split())
if n == 1 or m == 1:
    if n == m:
        print(1)
    else:
        print(max(n, m)-2)
elif n == 2 or m == 2:
    print(0)
else:
    print((n-2)*(m-2))
