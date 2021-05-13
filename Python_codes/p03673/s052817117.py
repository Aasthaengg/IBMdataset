n = int(input())
a = list(map(int,input().split()))

if n % 2 == 0:
    x = n//2
    for i in range(x):print(a[(n-1)-(2*i)])
    for i in range(x):print(a[2*i])
else:
    x = n//2 + 1
    for i in range(x):print(a[(n-1)-(2*i)])
    for i in range(x-1):print(a[(2*i)+1])