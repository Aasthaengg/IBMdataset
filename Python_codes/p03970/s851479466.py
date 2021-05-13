s = str(input())
cnt = 0
S = "CODEFESTIVAL2016"
for i in range(len(s)):
    if s[i] != S[i]:
        cnt += 1
print(cnt)