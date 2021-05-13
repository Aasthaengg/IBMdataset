s = input()
ans = 0
for bit in range(2 ** (len(s) - 1)):
    i = 0
    tmp = []
    for j in range(1, len(s) + 1):
        if j != len(s) and bit >> (j - 1) & 1 == 0: continue
        tmp.append(int(s[i:j]))
        i = j
    ans += sum(tmp)
print(ans)