n = int(input())
S = [input() for _ in range(n)]
XA = 0
BA = 0
BX = 0
cnt = 0
for s in S:
    cnt+=s.count('AB')
    if s[0]!='B' and s[-1]=='A':
        XA+=1
    elif s[0]=='B' and s[-1]=='A':
        BA+=1
    elif s[0]=='B' and s[-1]!='A':
        BX+=1
if BA==0:
    cnt+=min(XA,BX)
else:
    if XA+BX>0:
        cnt+=min(XA,BX)+BA
    else:
        cnt+=BA-1
print(cnt)