n = int(input())
a = list(map(int, input().split()))

ans = [0] * n

for i in reversed(range(1, n+1)):
    count = 0
    for j in range(2 * i, n + 1, i):
        count += ans[j-1]

    if count % 2 != a[i-1]:
        ans[i-1] = 1

print(sum(ans))
for i in range(n):
    if ans[i] == 1:
        print(i + 1)
