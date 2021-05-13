S = input()

ans = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        sub_s = S[i:j+1]
        is_acgt = True
        for s in sub_s:
            if s == "A" or s == "C" or s == "G" or s == "T":
                continue
            else:
                is_acgt = False
        if is_acgt:
            ans = max(ans, len(sub_s))

print(ans)
