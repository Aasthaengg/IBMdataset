s = input()

def solve(x):
    l = []
    for c in x:
        if c in l:
            return False
        l.append(c)
    return True

if solve(s):
    print('yes')
else:
    print('no')