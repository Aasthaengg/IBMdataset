s = input()
s_len = len(s)
check = s[0]
if s_len == 2 and s[0] != s[1]:
    print(2)
    exit()
s = s+"1"
ind = 0
ans = 1
for i in range(1,s_len):
    if check == s[ind+1]:
       check = s[ind+1:ind+3]
       ind += 1
    else:
       check = s[ind+1]
    ind += 1
    ans += 1
    if ind >= s_len-1:
        break
if ind == s_len and s[s_len-1] == s[s_len-2]:
    ans -= 1
print(ans)