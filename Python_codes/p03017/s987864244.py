n,a,b,c,d = map(int,input().split())
s = input()
ng = '##'
if c < d:
    if (ng in s[b-1:d]) or (ng in s[a-1:c]):
        print('No')
    else:
        print('Yes')
else:
    if ('...' not in s[b-2:d+1]):
        print('No')
    else:
        print('Yes')