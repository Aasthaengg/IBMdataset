

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def has_vacant(l, r, l_g, r_g):
    if l_g == r_g:
        if (r-l)%2 == 1:
            return True
    if l_g != r_g:
        if (r-l)%2 == 0:
            return True
    return False


def interact(l, r, l_g, r_g):
    m = (l+r)//2
    print(m)
    g = input()
    if g == 'Vacant':
        return
    if has_vacant(l, m, l_g, g):
        return interact(l, m, l_g, g)
    if has_vacant(m, r, g, r_g):
        return interact(m, r, g, r_g)


def solve():
    """
    0 1 2 3 4 5 6 7 8
    M       M     
    """
    N = read_int()
    l, r = 0, N-1
    print(l)
    l_g = input()
    if l_g == 'Vacant':
        return
    print(r)
    r_g = input()
    if r_g == 'Vacant':
        return
    interact(l, r, l_g, r_g)


if __name__ == '__main__':
    solve()
