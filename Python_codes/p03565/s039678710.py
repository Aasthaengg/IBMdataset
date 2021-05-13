s = list(input())
t = list(input())

l1, l2 = len(s), len(t)

res = ['z'] * l1
flag2 = False
for i in range(l1-l2+1):
    tmp_s = s.copy()
    flag1 = True
    for j in range(l1):
        if j < i or i + l2 <= j:
            if tmp_s[j] == '?':
                tmp_s[j] = 'a'
        else:
            if tmp_s[j] == t[j-i]:
                continue
            elif tmp_s[j] == '?':
                tmp_s[j] = t[j-i]
            else:
                flag1 = False

    if flag1:
        flag2 = True
        res = min(res, tmp_s)

if flag2:
    print(''.join(res))
else:
    print('UNRESTORABLE')