n = int(input())
s= list(input() for i in range(n))

acnt =0
bcnt =0
ecnt =0
cnt=0
nomal =0

for i in range(n):
    nomal += s[i].count('AB')
    t=0
    if s[i][0] == 'B':
        bcnt += 1
        cnt+=1
        t+=1
    if s[i][-1] == 'A':
        acnt += 1
        if not t:
            cnt+=1
        t+=1
    if t==2 :
        ecnt+=1

if cnt != 0 and cnt == ecnt:
    print(nomal + acnt-1)
else:
    print(nomal + min(acnt,bcnt))

