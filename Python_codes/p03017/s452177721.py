import sys
n, a, b, c, d = map(int, input().split())
s = input()
for i in range(a+1, c-1):
    if s[i-1]==s[i]=='#':
        print('No')
        sys.exit()
for i in range(b+1, d-1):
    if s[i-1]==s[i]=='#':
        print('No')
        sys.exit()
if c<d:
    print('Yes')
else:
    for i in range(b-1, d):
        if s[i-1]==s[i]==s[i+1]=='.':
            print('Yes')
            sys.exit()
    print('No')