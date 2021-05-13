import sys

N, T = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

# 利益の最大額
max_profit = 0
max_count = 0
# その時点での最小金額
tmp_min = float("inf")
# 売買金額のカウント
count = {}

for i in range(N-1):
    if A[i] not in count:
        count[A[i]] = 0
    count[A[i]] += 1

    if tmp_min > A[i]:
        tmp_min = A[i]

    profit = A[i+1] - tmp_min
    if max_profit < profit:
        max_profit = profit
        max_count = 1
    elif max_profit == profit:
        max_count += 1

    # print("max_profit", max_profit, "tmp_min", tmp_min)

print(max_count)