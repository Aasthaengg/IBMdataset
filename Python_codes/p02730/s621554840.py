s = input()
n = len(s)
flag = 0

if s == s[::-1]:
    flag += 1

ss = s[:int((n-1)/2)]
if ss == ss[::-1]:
    flag += 1

sss = s[int((n+3)/2)-1:]
if sss == sss[::-1]:
    flag += 1

if flag == 3:
    print('Yes')
else:
    print('No')