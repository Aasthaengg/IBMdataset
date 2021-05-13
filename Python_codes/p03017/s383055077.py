n, a, b, c, d = map(int, input().split())
s = input()

a -= 1
b -= 1
c -= 1
d -= 1

if '##' in s[a:max(c,d)+1]:
    print('No')
    exit()

if c < d:
    print('Yes')
else:
    if '...' in s[b-1:d+2]:
        print('Yes')
    else:
        print('No')