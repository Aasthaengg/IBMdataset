n = int(input())
a = list(map(int, input().split()))

ans = [0] * n
for i in range(n - 1, -1, -1):
    sum = 0
    for j in range(i + i + 1, n, i + 1):
        sum += ans[j]

    ans[i] = a[i] - sum
    ans[i] %= 2

print(ans.count(1))

for i in range(n):
    if ans[i] == 1:
        print(i + 1, end=" ")
