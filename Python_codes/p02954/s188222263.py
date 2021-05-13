s=list(input())

res=[0]*len(s)

ln=len(s)

pref=[0]*ln
suf=[0]*ln
cur=-1
for n in range(ln-1,-1,-1):
    if s[n]=='L':
        cur=n
    pref[n]=cur
cur=-1
for n in range(ln):
    if s[n]=='R':cur=n
    suf[n]=cur

for n in range(ln):
    if s[n]=='R':
        j=pref[n]-n-1
        if j%2:
            res[pref[n]]+=1
        else:
            res[pref[n]-1]+=1

    else:
        j= suf[n]-n-1

        if j%2:
            res[suf[n]]+=1
        else:
            res[suf[n]+1]+=1

print(*res)

