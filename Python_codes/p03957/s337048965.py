def solve():
    S = input()
    flag_c = False
    flag_f = False
    ans = ''
    for s in S:
        if s == 'C':
            flag_c = True
        if flag_c and s == 'F':
            flag_f = True
    if flag_c and flag_f:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solve()