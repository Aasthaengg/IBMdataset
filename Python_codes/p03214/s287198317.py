n = int(input())
a = list(map(int, input().split(' ')))
avg = 0
for i in range(n):
    avg += a[i]
avg /= n
delta = 100
ans = -1
for i in range(n):
    d = abs(avg - a[i])
    if d < delta:
        ans = i
        delta = d
print(ans)
