s = input()
res = 0


for i in range(len(s)):
    cnt = 0
    for j in range(i, len(s)):
        if s[j] == "A" or s[j] == "C" or s[j] == "T" or s[j] == "G": cnt += 1
        else: break
    res = max(res, cnt)
print(res)
