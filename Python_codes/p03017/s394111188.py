n, a, b, c, d = map(int, input().split())
s = input()

if c < d:
    if s[a-1:c].find('##')==-1 and s[b-1:d].find('##')==-1:
        print('Yes')
    else:
        print('No')
else:
    if s[a-1:c].find('##')==-1 and s[b-1:d].find('##')==-1 and s[b-2:d+1].find('...')!=-1:
        print('Yes')
    else:
        print('No')