s = input()
ans = 0
s_len = len(s)
dum = "CODEFESTIVAL2016"
for i in range(s_len):
    if s[i] != dum[i]:
        ans += 1
print(ans)