def solve():
    s = input()
    front = int(s[:2])
    back = int(s[2:])
    if 1 <= front <= 12 and 1 <= back <= 12:
        print('AMBIGUOUS')
    elif 1 <= front <= 12:
        print('MMYY')
    elif 1 <= back <= 12:
        print('YYMM')
    else:
        print('NA')


if __name__ == '__main__':
    solve()
