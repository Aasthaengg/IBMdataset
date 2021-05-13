n = int(input())
s = input()

a = [0] * (n + 1)
b = [0] * (n + 1)

for i in range(n):
    #先頭からi番目までの#の数
    if s[i] == '#':
        a[i + 1] = 1
    #末尾からi番目までの.の数
    if s[n - i - 1] == '.':
        b[n - i - 1] = 1
    #累積和をとる
    a[i + 1] += a[i]
    b[n - i - 1] += b[n - i]

ans = 100100100

for i in range(n):
    #i番目を境に分けた時に入れ替える数の最小値
    ans = min(ans, a[i] + b[i + 1])

print(ans)