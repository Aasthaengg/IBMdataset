n,a,b,c,d = map(int,input().split())

s=input()

s=list(s)

for i in range(a,max(c,d)):
    if s[i-1] == s[i] == '#':
        print('No')
        exit()

if c < d:
    print('Yes')
else:
    for i in range(b-2,d-1):
        if s[i] == s[i+1] == s[i+2] == '.':
            print('Yes')
            exit()
    print('No')