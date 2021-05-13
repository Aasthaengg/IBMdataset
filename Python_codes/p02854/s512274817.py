n = int(input())
a = list(map(int,input().split()))
m = 10**10
x = sum(a)
y = 0
for i in range(n):
    x -= a[i]
    y += a[i]
    m = min(abs(x-y),m)
print(m)