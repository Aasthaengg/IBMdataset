s_lst = list(map(str, input().split()))
ans = ''
for i in range(3):
    s = s_lst[i]
    ans += s[0]

print(ans.upper())