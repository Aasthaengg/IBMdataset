n = int(input())
d,x = map(int,input().split())
a = list(int(input()) for i in range(n))

for i in range(n):
    p = 1
    while p <= d:
        x += 1
        p += a[i]

print(x)