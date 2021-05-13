S = input()
ans = 0
n = len(S)
for i in range(2 ** (n - 1)):
    ex = S[0]
    for j in range(n - 1):
        if (i >> j) & 1:
            ex += "+"
        ex += S[j + 1]
    ans += eval(ex)
print(ans)