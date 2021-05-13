s = input()

tmp = ""
cnt = 0
ans = 0
flag = False  # skip用
for i in range(0, len(s) - 1):
    if flag:
        flag = False
        continue
    if s[i] == "A":
        cnt += 1
    elif s[i] + s[i + 1] == "BC":
        ans += cnt
        flag = True
    else:
        cnt = 0

print(ans)