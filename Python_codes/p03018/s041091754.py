import sys

readline = sys.stdin.buffer.readline


sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = readline().decode('utf-8')
    S = S.replace('BC', 'D')

    count_a = 0
    ans = 0

    for s in S:
        if s == 'A':
            count_a += 1
        elif s == 'D':
            ans += count_a
        else:
            count_a = 0

    print(ans)


if __name__ == '__main__':
    main()
