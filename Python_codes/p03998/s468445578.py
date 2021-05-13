import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = readline().strip()
    B = readline().strip()
    C = readline().strip()

    A = list(A[::-1])
    B = list(B[::-1])
    C = list(C[::-1])

    P = A
    x = 'a'
    while True:
        if not P:
            if x == 'a':
                print('A')
            elif x == 'b':
                print('B')
            else:
                print('C')
            break
        x = P.pop()
        if x == 'a':
            P = A
        elif x == 'b':
            P = B
        else:
            P = C

    return


if __name__ == '__main__':
    main()
