def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    s = input().rstrip('\n')

    r = s.count('R')
    if r > N-r:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
