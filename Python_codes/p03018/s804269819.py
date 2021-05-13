s = input()
n = len(s)
stat = 0
a = 0
bc = 0
abc = 0
ans = 0
def count():
    global ans, a, bc, abc
    newa = a+abc
    cnt = abc
    while cnt>0:
        ans += cnt
        cnt -= 1
        if a>0:
            a -= 1
            cnt += 1
        if bc>0:
            bc -= 1
            cnt += 1
    a = newa
    bc = 0
    abc = 0
i = 0
while i<n:
    if stat==0:
        if s[i:i+3]=='ABC':
            a = 0
            abc = 1
            stat = 2
            i += 3
        elif s[i]=='A':
            a = 1
            stat = 1
            i += 1
        else:
            i += 1
    elif stat==1:
        if s[i:i+3]=='ABC':
            abc = 1
            stat = 2
            i += 3
        elif s[i]=='A':
            a += 1
            i += 1
        else:
            stat = 0
    elif stat==2:
        if s[i:i+3]=='ABC':
            abc += 1
            i += 3
        elif s[i:i+2]=='BC':
            bc = 1
            stat = 3
            i += 2
        else:
            count()
            stat = 1
    else:
        if s[i:i+2]=='BC':
            bc += 1
            i += 2
        else:
            count()
            stat = 1
if stat>=2:
    count()
print(ans)