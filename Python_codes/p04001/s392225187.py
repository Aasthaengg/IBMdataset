S = input()
N = len(S)

ans = 0
for i in range(2 ** (N - 1)):
    ptn = [' '] * (N - 1)
    for j in range(N - 1):
        if (i >> j) & 1:
            ptn[len(ptn) - j - 1] = '+'

    formula = ''.join([n + op for n, op in zip(list(S), ptn + [''])]).replace(' ', '')
    ans += eval(formula)

print(ans)