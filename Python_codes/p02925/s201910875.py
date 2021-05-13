import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    def calc_id(x, y):
        return min(x, y) * 10007 + max(x, y)

    from collections import defaultdict, Counter, deque
    from copy import copy

    n = int(readline())

    edge = defaultdict(list)
    count = Counter()

    for x in range(1, n + 1):
        a = list(map(int, readline().split()))
        count[calc_id(x, a[0])] += 0
        for j in range(n - 2):
            y = a[j]
            z = a[j + 1]
            u_id = calc_id(x, y)
            v_id = calc_id(x, z)
            edge[u_id].append(v_id)
            count[v_id] += 1

    ans = 0
    rem = n * (n - 1) // 2
    que = deque()
    for key, val in count.items():
        if val == 0:
            que.append(key)
    que_tomorrow = deque()

    while rem:
        ans += 1
        if not que:
            print(-1)
            return
        while que:
            cur_match = que.popleft()
            for nx_match in edge[cur_match]:
                count[nx_match] -= 1
                if count[nx_match] == 0:
                    que_tomorrow.append(nx_match)
            rem -= 1
        que = copy(que_tomorrow)
        que_tomorrow.clear()

    print(ans)


if __name__ == '__main__':
    main()
