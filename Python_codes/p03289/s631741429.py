s = input()

f = True
if s[0] != 'A':
    f = False
else:
    cnt=0
    for _s in s[2:-1]:
        if _s == 'C':
            cnt+=1
    if cnt!=1:
        f = False
    else:
        cnt = 0
        for _s in s:
            if _s.isupper():
                cnt+=1
        if cnt>2:
            f = False
if f:
    print('AC')
else:
    print('WA')


