S = input()
ret = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        f = True
        for k in S[i:j + 1]:
            if k not in ("ACGT"):
                f = False
                break
        if f:
            ret = max(ret, (j + 1) - i)
print(ret)