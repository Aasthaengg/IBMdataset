n = int(input())
a = list(map(int ,input().split()))

x = 1000
for i in range(n-1):
    l = a[i]
    r = a[i+1]
    if (l < r):
        k = x//l
        x %= l
        x += k*r

print(x)