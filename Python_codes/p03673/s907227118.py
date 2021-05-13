n = int(input())
a = list(map(int,input().split()))
start = n - 1
while start >= 0:
    print(a[start],end=' ')
    start -= 2
if n % 2 == 0:
    start = 0
else:
    start = 1
while start < n:
    print(a[start],end=' ')
    start += 2
