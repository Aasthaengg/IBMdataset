s=list(input())
n=len(s)+1
lc=[0]
rc=[0]
for i in range(n-1):
    if s[i]=='<':
        lc.append(lc[-1]+1)
    else:
        lc.append(0)
    if s[-1-i]=='>':
        rc.append(rc[-1]+1)
    else:
        rc.append(0)
rc=rc[::-1]
ans=[max(lc[i], rc[i]) for i in range(n)]
print(sum(ans))