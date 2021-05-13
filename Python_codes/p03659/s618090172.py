# 累積じゃね
n = int(input())
arr = list(map(int, input().split()))
ruiseki = [0] * (n + 1)
for i in range(1, n + 1):
    ruiseki[i] = ruiseki[i - 1] + arr[i - 1]
ans = 10**10
for i in range(1, n):
    takahashi = ruiseki[i]
    raskal = ruiseki[n] - takahashi
    ans = min(ans, abs(raskal - takahashi))
print(ans)