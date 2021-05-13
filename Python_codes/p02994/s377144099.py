# 総価からの最小誤差を求める。
n, l = map(int, input().split())
s = []
# リンゴの味
for i in range(1, n+1):
    s.append(l+i-1)
# リンゴの最小誤差を求める絶対値です。
a = 10**19
# リンゴの最小誤差の変数です。
h = 0
for i in range(n):
    # 最小誤差を判定します。
    if a > abs(s[i]):
        a = abs(s[i])
        h = s[i]
# 総価から最小誤差を引いた味です。
print(sum(s)-h)
