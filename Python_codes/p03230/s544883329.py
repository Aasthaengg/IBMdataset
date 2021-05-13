import sys
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():
    N = in_n()

    for i in range(1, N + 1):
        if i * (i + 1) == N * 2:
            X = i
            break
    else:
        print('No')
        exit()

    ans = [[] for _ in range(X + 1)]
    ans[0] = [t for t in range(1, X + 1)]
    non_used = deque(range(X + 1, N + 1))
    used = [deque(range(1, X + 1))]

    for i in range(1, X + 1):
        for u in used:
            ans[i].append(u.popleft())

        size = len(ans[i])
        t = []
        for j in range(X - size):
            t.append(non_used.popleft())

        if t:
            ans[i] += t
            used.append(deque(t))

    print('Yes')
    print(X + 1)
    for a in ans:
        print(' '.join(map(str, [X] + a)))


if __name__ == '__main__':
    main()
