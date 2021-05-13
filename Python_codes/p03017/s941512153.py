n, a, b, c, d = map(lambda x: int(x)-1, input().split())
s = input()


def can_reach(x, y):
    return '##' not in s[x:y+1]


def can_jump(x, y):
    return '...' in s[x-1:y+2]


if can_reach(a, c) and can_reach(b, d):
    if c < d:
        print('Yes')
    else:
        if can_jump(b, d):
            print('Yes')
        else:
            print('No')
else:
    print('No')
