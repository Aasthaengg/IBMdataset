import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 正負が混在するか判定
plus = False
minus = False
for a in A:
    if a > 0:
        plus = True
    elif a < 0:
        minus = True

ans = []

# 正負が混在する場合、符号を揃える
if plus == True and minus == True:
    max_a = max(A)
    min_a = min(A)
    max_idx = A.index(max_a)
    min_idx = A.index(min_a)
    # 正に揃える
    if abs(max_a) >= abs(min_a):
        for i in range(N):
            A[i] += max_a
            ans.append([max_idx + 1, i + 1])
    # 負に揃える
    if abs(max_a) < abs(min_a):
        for i in range(N):
            A[i] += min_a
            ans.append([min_idx + 1, i + 1])
# print(A)

# 正に揃っている場合
if min(A) >= 0:
    # 前から累積和
    for i in range(1, N):
        A[i] += A[i - 1]
        ans.append([i, i + 1])
# 負に揃っている場合
else:
    # 後ろから累積和
    for i in range(N - 2, -1, -1):
        A[i] += A[i + 1]
        ans.append([i + 2, i + 1])

print(len(ans))
for a in ans:
    print(*a)
# print(A)
