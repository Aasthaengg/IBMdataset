import bisect

S = list(str(input()))
T = list(str(input()))

X = [[] for _ in range(26)]
for i, c in enumerate(S):
    # a = 0, b = 1, ..., z = 25
    j = ord(c) - ord('a')
    X[j].append(i + 1)

# print(X)

# Sの繰り返し数
div_cnt = 0
# 現在のindex
now = 0

for c in T:
    # a = 0, b = 1, ..., z = 25
    j = ord(c) - ord('a')

    # Sにない文字がTにある場合
    if len(X[j]) == 0:
        print(-1)
        exit()

    next = bisect.bisect_right(X[j], now)
    # print(c,now,next)

    if next == len(X[j]):
        div_cnt += 1
        now = X[j][0]
    else:
        now = X[j][next]

ans = div_cnt * len(S) + now
print(ans)
