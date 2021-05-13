s = str(input())
t = str(input())
ds = {chr(i+97): -1 for i in range(26)}
dt = {chr(i+97): -1 for i in range(26)}
for i in range(len(s)):
    if ds[s[i]] >= 0:
        if ds[s[i]] != ord(t[i]):
            print('No')
            break
    if dt[t[i]] >= 0:
        if dt[t[i]] != ord(s[i]):
            print('No')
            break
    if ds[s[i]] < 0:
        ds[s[i]] = ord(t[i])
    if dt[t[i]] < 0:
        dt[t[i]] = ord(s[i])
else:
    print('Yes')
