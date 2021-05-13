# n: 数列の項数　m: 数列の和
# d=公約数とすると、数列は全項がdの倍数である
# よって数列の和もdの倍数である
# ゆえに、dはmの約数である
n, m = map(int, input().split())

def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


d = divisor(m)
ans = 0
for i in d:
    # i: mの約数。数列の公約数でもある。
    # 公約数 * nが、mを超えない範囲で最大の公約数を求める
    if i * n <= m:
        ans = max(i, ans)

print(ans)