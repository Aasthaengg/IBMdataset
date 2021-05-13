s=list(input())
t=list(input())

ok = False
for i in range(len(s)):
    if s==t:
        ok=True
        break
    s = [s[i-1] for i in range(len(s))]
    
if ok:
    print('Yes')
else:
    print('No')