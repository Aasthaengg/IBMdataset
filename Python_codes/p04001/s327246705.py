S = input()
ans = 0
for i in range(2 ** (len(S) - 1)):
    txt = S[0]
    for j in range(len(S) - 1):
        if i >> j & 1:
            txt += " " + S[j + 1]
        else:
            txt += S[j + 1]
    ans += sum(list(map(int, txt.split())))
print(ans)