n, m = [int(i) for i in input().split()]
if n == m == 1:
    print(1)
elif n == 1 or m == 1:
    print(n*m-2)
else:
    print((n-2)*(m-2))