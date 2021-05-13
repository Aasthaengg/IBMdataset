from statistics import median
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] -= i+1

med = median(a)
ans = 0

for i in range(n):
    ans += abs(a[i] - med)

print(int(ans))