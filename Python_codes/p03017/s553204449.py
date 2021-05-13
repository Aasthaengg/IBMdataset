n,a,b,c,d = map(int,input().split())
s = '.'+input()
i=a
f = True
while i<c:
    if s[i+1]=='.':
        i += 1
    elif i<c-1 and s[i+2]=='.':
        i += 2
    else:
        f = False
        break
i = b
ok = False
while i<d:
    if s[i-1:i+2]=='...':
        ok = True
    if s[i+1]=='.':
        i += 1
    elif i<d-1 and s[i+2]=='.':
        i += 2
    else:
        f = False
        break
if d<n and s[d-1:d+2]=='...':ok=True
if d<c and not ok:f=False
print('Yes' if f else 'No')