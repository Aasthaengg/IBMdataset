s = list(input())
n = len(s)
ans = 10**19
# 連続する３つの数字と比較する。
for i in range(1, n-1):
    a = int("".join([s[i-1], s[i], s[i+1]]))
    ans = min(abs(753-a), ans)
print(ans)
