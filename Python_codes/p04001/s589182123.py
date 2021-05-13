FS, *S = input()
L = len(S)
ans = 0
for bit in range(1 << L):
    tmp = FS
    f = []
    for i, s in enumerate(S):
        if bit >> i & 1:
            f.append(tmp)
            tmp = s
        else:
            tmp += s
    f.append(tmp)
    ans += sum(map(int, f))
print(ans)
