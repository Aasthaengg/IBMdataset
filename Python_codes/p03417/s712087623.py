n, m = map(int, input().split())
if n == 1 and m == 1:
    print(1)
elif n == 1 or m == 1:
    n, m = sorted([n, m])
    print(n*m-2)
else:
    print(n*m-2*(n+m)+4)