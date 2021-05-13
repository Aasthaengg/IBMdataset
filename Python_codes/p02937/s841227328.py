import bisect

# d := {"a":[], "b":[], ..., "z":[]}
d = {}
key = list("abcdefghijklmnopqrstuvwxyz")
for i in range(26):
    d[key[i]] = []

# 1文字ずつ分割してリスト化
S = list(input())
N = len(S)

T = list(input())
M = len(T)

for i in range(N):
    d[S[i]].append(i + 1)

# print(d)

S_set = set(S)

ans = 0
now = 0
# Tの1文字目, 2文字目, ...
for i in range(M):
    if T[i] in S_set:
        next = bisect.bisect_right(d[T[i]], now)
        # print("i,next = ", i, next)
        # 右端ではない場合
        if next < len(d[T[i]]):
            now = d[T[i]][next]
        # 右端になる場合
        else:
            now = d[T[i]][0]
            ans += N
    else:
        print(-1)
        exit()

ans += now
print(ans)
