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

    if len(A) > len(B):
        ans = 'GREATER'
    elif len(A) < len(B):
        ans = 'LESS'
    else:
        ans = 'EQUAL'
        for a, b in zip(A, B):
            if int(a) > int(b):
                ans = 'GREATER'
                break
            elif int(a) < int(b):
                ans = 'LESS'
                break

    print(ans)

    return


if __name__ == '__main__':
    main()
