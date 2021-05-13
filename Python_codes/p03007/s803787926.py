import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque

    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    cur = max(a)
    a = a[:n - 1]

    neg = []
    pos = []

    for x in a:
        if x <= 0:
            neg.append(x)
        else:
            pos.append(x)

    seq = []

    if pos:
        pos_que = deque()
        pos_que.extend(pos)
        if neg:
            cur2 = neg.pop()
        else:
            cur2 = pos_que.popleft()
        while pos_que:
            y = pos_que.popleft()
            seq.append([cur2, y])
            cur2 = cur2 - y
        seq.append([cur, cur2])
        cur -= cur2

    for y in neg:
        seq.append([cur, y])
        cur = cur - y

    print(cur)
    for i in range(n - 1):
        print(*seq[i])


if __name__ == '__main__':
    main()
