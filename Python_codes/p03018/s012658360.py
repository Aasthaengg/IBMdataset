s = str(input())
s = s.replace('BC', 'D')
#print(s)
S = []
temp = []
for c in s:
    if c == 'A' or c == 'D':
        temp.append(c)
    else:
        if temp:
            S.append(temp)
            temp = []
else:
    if temp:
        S.append(temp)
#print(S)
ans = 0
for s in S:
    cnt = 0
    for j in range(len(s)):
        if s[j] == 'A':
            cnt += 1
        else:
            ans += cnt
print(ans)
