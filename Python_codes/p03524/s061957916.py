s = input()
n = len(s)

dic = {}
for i in range(n):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1

if len(dic) == 1:
    if n == 1:
        print('YES')
    else:
        print('NO')
elif len(dic) == 2:
    if n == 2:
        print('YES')
    else:
        print('NO')
else:
    maxi = max(dic.values())
    mini = min(dic.values())
    if maxi - mini <= 1:
        print('YES')
    else:
        print('NO')