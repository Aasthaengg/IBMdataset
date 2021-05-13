n, a, b, c, d = map(int, input().split())
s = input()

s = '#' + s + '#'

def can_reach(start, end):
    for i in range(start, end+1):
        if s[i] == '#' and s[i+1] == '#':
            return False
    return True

if not can_reach(a, b) or not can_reach(b, d):
    print('No')
    exit()

if c > d:
    can_over = False
    for i in range(b, d+1):
        if s[i-1] == '.' and s[i] == '.' and s[i+1] == '.':
            can_over = True
    if not can_over:
        print('No')
        exit()

print('Yes')
