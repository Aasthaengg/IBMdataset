s = input()
t = input()

ls = len(s)
lt = len(t)

if ls < lt:
    print('UNRESTORABLE')
    exit()
anslist = []
for i in range(ls-lt+1):
    flag = True
    for j in range(lt):
        if s[i+j] != '?' and s[i+j] != t[j]:
            flag = False
    if flag:
        anslist.append(i)
if anslist:
    i = max(anslist)
    x = s[:i] + t + s[i+lt:]
    print(x.replace('?','a'))
else:
    print('UNRESTORABLE')