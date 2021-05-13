s = input()
n = len(s)
ok = True
for i in range(n):
    cnt = s.count(s[i])
    if cnt > 1:
        ok = False

if ok:
    print('yes')
else:
    print('no')