import statistics
n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    x[i] -= i+1

b = statistics.median(x)

ans = 0
for i in range(n):
    ans += abs(x[i] - b)

print(int(ans))
