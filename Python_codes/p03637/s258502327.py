import sys
read = sys.stdin.read
def main():
    n = int(input())
    a = list(map(int, read().split()))
    odd = 0
    div4 = 0
    div2 = 0
    for ae in a:
        odd += ae % 2 != 0
        div4 += ae % 4 == 0
        div2 += ae % 2 == 0 and ae % 4 != 0
    div2r = div2 % 2
    if odd +div2r  > div4 + 1:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
