mod = 10 ** 9 + 7

def bekizyo(x, n): #べき乗x**n(nが大きいとき)
    n2 = format(n, "b")
    l_n2 = len(n2)
    ass = 1
    y = x
    for i in range(l_n2):
        if n2[l_n2 - 1 - i] == "1":
            ass *= y
            ass %= mod
        y **= 2
        y %= mod
    return ass


n,k = map(int, input().split())

l = [0] * (k+1)

for i in range(k, 0, -1):
    num = bekizyo(k//i, n)
    for j in range(k//i - 1):
        num -= l[i * (j+2)]
        num %= mod
    l[i] = num

ans = 0

for i in range(1, k+1):
    ans += i * l[i]
    ans %= mod

print(ans)