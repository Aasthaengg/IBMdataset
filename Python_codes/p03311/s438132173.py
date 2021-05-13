import statistics
n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    x[i] -= i+1

x.sort()
x_ = []
b = 0
if x.count(0) <= n//2:
    for i in range(n):
        if x[i] != 0:
             x_.append(x[i])

    b = statistics.median(x_)

ans = 0
for i in range(n):
    ans += abs(x[i] - b)

print(int(ans))