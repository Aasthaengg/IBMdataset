# なんかまともに考えるとわからん
# テキトーに問題文読まずサンプルだけ眺めるとgcdになる

n = int(input())
a = list(map(int, input().split()))
ans = a[0]


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    while a > 0:
        a, b = b % a, a
    return b


for i in range(1, n):
    ans = gcd(ans, a[i])
print(ans)