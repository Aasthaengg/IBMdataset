n,a,b,c,d = map(int,input().split())
s = list(input())
s.insert(0,0)
for i in range(a,max(c,d)):
    if '#' == s[i] and '#' == s[i+1]:
        print('No')
        exit(0)
if c < d:
    print('Yes')
else:
    for i in range(b-1,d):
        if '.' == s[i] and '.' == s[i+1] and '.' == s[i+2]:
            print('Yes')
            exit(0)
    print('No')