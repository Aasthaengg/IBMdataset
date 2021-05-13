n, a, b, c, d = map(lambda x: int(x)-1, input().split())
s = input()


def can_reach(x, y):
    return 0 == s[x:y+1].count('##')


def can_reach_cross(x, y, a, b):
    t = s[x:y+1]
    if 0 != t.count('##'):
        return False
    if '...' in s[a-1:b+2]:
        return True
    return False


if c < d:
    # parallel
    if can_reach(a, c) and can_reach(b, d):
        print('Yes')
    else:
        print('No')
else:
    # cross
    if can_reach(b, d) and can_reach_cross(a, c, b, d):
        print('Yes')
    else:
        print('No')
