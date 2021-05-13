s = input()
t = ['A','C','G','T']

ans = 0
tmp_ans = 0
for i in s:
    if i in t:
        tmp_ans += 1
    else:
        ans = max(tmp_ans, ans)
        tmp_ans = 0
ans = max(tmp_ans, ans)
print(ans)