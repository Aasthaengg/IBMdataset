n, k = map(int, input().split())
s = input()
sl = []
for i in range(len(s)):
    sl.append(s[i])

Al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
al = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(Al)):
    if sl[k-1] == Al[i]:
        sl[k-1] = (al[i])


print(''.join(sl))