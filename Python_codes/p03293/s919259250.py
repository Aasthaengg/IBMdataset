s = input()
t = input()
flg = False

for i in range(len(s)):
    if s == t:
        flg = True
        break
    else:
        s = s[-1] + s[0:-1]        

if flg:
    print('Yes')
else:
    print('No')
