s = input()
t = input()
l = len(t)

if len(s)<l:
    print('UNRESTORABLE')   
    exit() 
for i in range(len(s),-1+l,-1):
    tmp = s[i-l:i]
    tmp_flag = False
    for j in range(l):
        if tmp[j]=='?':
            tmp_flag = True
        elif tmp[j]!=t[j]:
            tmp_flag = False
            break
        else:
            tmp_flag = True
    if tmp_flag:
        t = list(t)
        s = list(s)
        s[i-l:i] = t
        break

if tmp_flag:
    for i in range(len(s)):
        if s[i]=='?':
            s[i] = 'a'
    print(''.join(s))
else:
    print('UNRESTORABLE')
