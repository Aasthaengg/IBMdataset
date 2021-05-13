s2 = input()
t = input()

lst = []
for i in range(len(s2)-len(t)+1):
    moji = ''
    if s2[i] == t[0] or s2[i] == '?':
        moji = s2[:i]+t[0]

        flg = 0
        for j in range(1,len(t)):
            if s2[i+j] == t[j] or s2[i+j] == '?':
                moji += t[j]
            else:
                flg = 1
                break
        if flg == 0:
            lst.append(moji+s2[i+len(t):])

if not lst:
    print('UNRESTORABLE')
else:
    print(min(lst).replace('?','a'))

