string = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
ans = 100
for a in alpha:
    tmp = 0
    ans_tmp = 0
    for s in string:
        if s == a:
            ans_tmp = max(ans_tmp, tmp)
            tmp = 0
        else:
            tmp += 1
    ans_tmp = max(ans_tmp, tmp)
    ans = min(ans, ans_tmp)
print(ans)