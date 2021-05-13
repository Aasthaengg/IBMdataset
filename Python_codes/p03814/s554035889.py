s=input()
Acnt = 0
Zcnt = len(s)-1
while 1:
    if s[Acnt] == 'A':
        Acnt += 1
        break
    else:
        Acnt += 1
while 1:
    if s[Zcnt] == 'Z':
        Zcnt += 1
        break
    else:
        Zcnt -= 1
print(Zcnt-Acnt+1)