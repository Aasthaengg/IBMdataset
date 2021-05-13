def solve():
    s = input()
    if 'L' in s[::2]:
        print('No')
    elif 'R' in s[1::2]:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    solve()
