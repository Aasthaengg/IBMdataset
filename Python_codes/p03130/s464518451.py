import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    cnt = {1: 0, 2: 0, 3: 0, 4: 0}
    for _ in range(3):
        a, b = map(int, input().split())
        cnt[a] += 1
        cnt[b] += 1

    ans = 'YES'
    for k, v in cnt.items():
        if v > 2:
            ans = 'NO'
            break

    print(ans)


if __name__ == '__main__':
    main()
