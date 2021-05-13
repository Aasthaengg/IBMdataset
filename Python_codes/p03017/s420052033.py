import sys
n, a, b, c, d = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

def can_reach(start, end):
    for i in range(start, end):
        if s[i] == '#' and s[i+1] == '#':
            return False
    return True

if can_reach(a-1, c-1) and can_reach(b-1, d-1):
    if c < d:
        print('Yes')
    else:
        flag = False
        for i in range(b-1, d):
            if s[i-1] == '.' and s[i] == '.' and s[i+1] == '.':
                flag = True
        print('Yes' if flag else 'No')
else:
    print('No')
