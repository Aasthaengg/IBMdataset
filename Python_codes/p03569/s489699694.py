s = input()
LS = len(s)
rs = s[::-1]
lc = []
rc = []
lx = 0
rx = 0
for i in range(LS):
    if s[i] != 'x':
        lc.append(s[i])
    if rs[i] != 'x':
        rc.append(rs[i])
cnt = 0
if lc==rc or len(lc)+len(rc)==1:
    i = 0
    j = LS-1
    while j>i:
        if s[i]!=s[j]:
            if s[i]=='x':
                cnt+=1
                i +=1
            elif s[j]=='x':
                cnt+=1
                j -=1
        else:
            i +=1
            j -=1
    print(cnt)
else:
    print(-1)