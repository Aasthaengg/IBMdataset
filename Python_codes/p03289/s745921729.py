s = input()

def has_A(x):
    if x[0] == 'A': return True
    return False


def has_C(x):
    if x[2:-1].count('C') == 1: return True
    return False


def is_lower_this_case(x):
    i = x.index('C')
    if x[1:i].islower() and x[i+1:].islower():
        return True
    return False

if has_A(s) and has_C(s) and is_lower_this_case(s):
    print('AC')
else:
    print('WA')