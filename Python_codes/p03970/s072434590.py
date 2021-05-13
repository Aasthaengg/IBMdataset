s = input()
ans = "CODEFESTIVAL2016"

cnt = 0
for i in range(len(s)):
	cnt += s[i] != ans[i]

print(cnt)