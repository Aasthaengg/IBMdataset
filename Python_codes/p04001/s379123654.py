S = input()
n = len(S)
res = 0
for i in range(1 << n-1):
    subres = 0
    subst = S[0]
    for j in range(n-1):
        if i >> j & 1:
            subres += int(subst)
            subst = S[j+1]
        else:
            subst += S[j+1]
        if j == n - 2:
            subres += int(subst)
    res += subres
if n == 1:
    print(int(S))
else:
    print(res)


