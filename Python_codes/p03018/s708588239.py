s = input()
s = s.replace('BC','D')
a_cnt = 0
before_s = 'A'
ans = 0
for i in range(len(s)):

    if s[i] == 'A':
        a_cnt += 1
        before_s = s[i]
    elif (s[i]=='D'):
        ans +=a_cnt
        before_s = 'A'
    else:
        a_cnt = 0
        before_s = s[i]

print(ans)