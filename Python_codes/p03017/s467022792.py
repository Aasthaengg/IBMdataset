n, a,b,c,d = map(int, input().split())
s = input()

def check_twice(left, right, l):
    for i in range(left-1, right):
        if l[i] == '#' and l[i+1] == '#':
            return False
    return True

def check_triple(left, right, l):
    f = False
    for i in range(left-1, right-2):
        if l[i] == '.' and l[i+1] == '.' and l[i+2] == '.':
            f = True
            break
        else:
            continue
    return f

if c < d:
    flg = check_twice(a, c, s) & check_twice(b, d, s)
    if flg is True:
        print('Yes')
    else:
        print('No')

else:
    flg = check_twice(a, c, s) & check_triple(b-1, d+1, s)
    if flg is True:
        print('Yes')
    else:
        print('No')
