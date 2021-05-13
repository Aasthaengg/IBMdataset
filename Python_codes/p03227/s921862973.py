s = input()
ans = []
if len(s) == 2:
    print(s)
elif len(s) == 3:
    for i in range(len(s)):
        ans.append(s[2-i])
    ans_ = map(str, ans)
    print("".join(ans_))