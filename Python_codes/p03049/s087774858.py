N = int(input())
S = [input() for i in range(N)]
ABcnt = 0
Acnt = 0
Bcnt = 0
BAcnt = 0
for s in S:
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'B':
            ABcnt += 1
    if s[0] == 'B' and s[-1] == 'A':
        BAcnt += 1
    elif s[0] == 'B':
        Bcnt += 1
    elif s[-1] == 'A':
        Acnt += 1

if Acnt == 0 and Bcnt == 0:
    ans = ABcnt + max(BAcnt-1,0)
else:
    ans = ABcnt + BAcnt + min(Acnt,Bcnt)

print(ans)
