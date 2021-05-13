import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = [set()] * 3
    S[0] = {1, 3, 5, 7, 8, 10, 12}
    S[1] = {4, 6, 9, 11}
    S[2] = {2}

    x, y = map(int, readline().split())

    ans = 'No'
    for s in S:
        if x in s and y in s:
            ans = 'Yes'
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
