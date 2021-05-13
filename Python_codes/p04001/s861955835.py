s = input()

ans = 0
n = len(s) - 1
for i in range(2 ** n):
    op = [''] * n
    for j in range(n):
        if ((i >> j) & 1):
            op[n - j - 1] = '+'
    f = ''

    for p_n, p_o in zip(s,op+['']):
        f += p_n + p_o
    ans += eval(f)

print(ans)