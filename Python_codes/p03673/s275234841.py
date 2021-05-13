n = int(input())
a = list(map(int,input().split()))
if n % 2 == 0:
    start = n - 1
    while start >= 0:
        print(a[start],end=' ')
        start -= 2
    start = 0
    while start < n:
        print(a[start],end=' ')
        start += 2
elif n % 2 == 1:
    start = n - 1
    while start >= 0:
        print(a[start],end=' ')
        start -= 2
    start = 1
    while start < n:
        print(a[start],end=' ')
        start += 2