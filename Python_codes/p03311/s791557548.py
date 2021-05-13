n = int(input())
a = list(map(int, input().split()))
b = [0] * n
ans = 0

for i in range(1, n+1):
    b[i-1] = a[i-1] - i

sort_b = sorted(b)
num = sort_b[n // 2]

for i in range(n):
    ans += abs(b[i] - num)

print(ans)