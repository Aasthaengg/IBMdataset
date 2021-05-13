a, b,c = map(int, input().split())
s=False
if a==b and b!=c:
    
    s=True
if a==c and b!=c:
    s=True
if c==b and a!=c:
    s=True
if s:
    print('Yes')
else:
    print('No')