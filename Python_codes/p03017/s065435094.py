n,a,b,c,d = map(int, input().split())
s = input()

if '##' in s[a-1:c] or '##' in s[b-1:d]:
    print('No')
else:
    if c<d:
        print('Yes')
    else:
        if '...' in s[b-2:d+1]:
            print('Yes')
        else:
            print('No')