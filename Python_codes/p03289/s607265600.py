s = input()
n = len(s)

f = False
ans = s[0] == 'A'
for i in range(1,n):
    if 'a' <= s[i] <= 'z': continue

    if not f and i>1 and i<n-1 and s[i] == 'C':
        f = True
        continue

    ans = False
    break

if ans and f:
    print('AC')
else:
    print('WA')
