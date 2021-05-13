s = list(str(input()))
t = list(str(input()))

pos = False
rep = list(range(len(s)-len(t)+1))
rep.reverse()
for i in rep:
    flag = True
    for j in range(len(t)):
        if s[i+j] == '?':
            pass
        elif s[i+j] == t[j]:
            pass
        else:
            flag = False

    if flag == False:
        continue
    for j in range(len(t)):
        s[i+j] = t[j]
    pos = True
    break

if pos == False:
    print('UNRESTORABLE')
else:
    for i in range(len(s)):
        if s[i] == '?':
            s[i] = 'a'
    print(''.join(s))