N, K = map(int, input().split())
S = input()

# https://drken1215.hatenablog.com/entry/2019/04/14/222900
# 1が連続する個数の列に直す

SS = []
if S[0] == '0':
    SS.append(0)
i = 0
while i < len(S):
    j = i
    while j < len(S) and S[j] == S[i]:
        j += 1
    SS.append(j - i)
    i = j
if S[-1] == '0':
    SS.append(0)

# print(SS)

# 累積和
sums = [0 for _ in range(len(SS) + 1)]
for i in range(len(SS)):
    sums[i + 1] = sums[i] + SS[i]
# print(sums)

# 偶数番目からはじまる長さ (2K + 1) 区間の総和
ans = 0
for left in range(0, len(sums), 2):
    right = left + K * 2 + 1
    if right >= len(sums): # 飛び越したら末尾まで
        right = len(sums) - 1
    ans = max(ans, sums[right] - sums[left])
print(ans)
