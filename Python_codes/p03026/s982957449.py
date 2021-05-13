import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque, defaultdict
    n = int(readline())
    edge = defaultdict(list)

    for _ in range(n - 1):
        a, b = map(int, readline().split())
        edge[a].append(b)
        edge[b].append(a)

    c = list(map(int, readline().split()))
    c.sort(reverse=True)

    nums = [0] * (n + 1)

    que = deque()
    que.append((1, 0))

    cnt = 0
    m = 0

    while que:
        cur, prev_num = que.popleft()
        num = c[cnt]
        nums[cur] = num
        m += min(num, prev_num)
        cnt += 1
        for nx in edge[cur]:
            if nums[nx] == 0:
                que.append((nx, num))

    print(m)
    print(*nums[1:])


if __name__ == '__main__':
    main()
