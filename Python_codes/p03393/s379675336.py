s = list(input())
alph = [chr(i) for i in range(97, 123)]
alph_count = [0] * 26
for i in s:
    alph_count[alph.index(i)] = 1
ans = ["-1"]
if len(s) != 26:
    for i in range(26):
        if alph_count[i] == 0:
            ans = s + [alph[i]]
            break
else:
    for i in range(25, -1, -1):
        c = -1
        for j in range(26):
            if s[i] == alph[j]:
                c = j
            if not c == -1:
                if alph_count[j] == 0:
                    s[i] = alph[j]
                    ans = s[0 : i + 1]
            if not ans[0] == "-1":
                break
        alph_count[c] = 0
        if not ans[0] == "-1":
            break
print("".join(ans))