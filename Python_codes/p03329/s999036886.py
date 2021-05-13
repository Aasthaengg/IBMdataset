n = int(input())

cnt = [float("inf")] * (n + 1)
cnt[0] = 0

sixes = [pow(6, num) for num in range(1, 10)]
nines = [pow(9, num) for num in range(1, 10)]

for six in sixes:
    for i in range(n + 1):
        if six + i <= n and cnt[i] != float("inf"):
            cnt[six + i] = min(cnt[six + i], cnt[i] + 1)

for nine in nines:
    for i in range(n + 1):
        if nine + i <= n and cnt[i] != float("inf"):
            cnt[nine + i] = min(cnt[nine + i], cnt[i] + 1)

for i in range(n):
    cnt[i + 1] = min(cnt[i + 1], cnt[i] + 1)

print(cnt[n])
