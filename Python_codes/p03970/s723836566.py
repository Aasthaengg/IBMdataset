s = input()
fact ='CODEFESTIVAL2016'

cnt = 0
for i in range(len(s)):
    if s[i] != fact[i]: cnt += 1
print(cnt)