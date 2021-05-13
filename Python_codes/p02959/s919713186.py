n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in range(n):
    c += min(a[i], b[i])
    if b[i]-a[i] >= a[i+1]:
        c += a[i+1]
        a[i+1] = 0
    else:
        c += max(b[i]-a[i], 0)
        a[i+1] = max(a[i+1] - max(b[i]-a[i], 0), 0)
print(c)