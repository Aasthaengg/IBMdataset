s = input()
l = len(s)
s += "D"*10
cnt = 0
ans = 0
i = 0
while i < l:
    if s[i] == "A": cnt += 1
    elif s[i:i+2] == "BC":
        ans += cnt
        i += 1
    else: cnt = 0
    i += 1
print(ans)