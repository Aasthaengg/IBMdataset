from collections import deque
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    n, q = map(int, input().split())
    node = [[]for _ in range(n)]
    looked = [1] * n
    for i in range(n - 1):
        a, b = map(int, input().split())
        node[b - 1].append(a - 1)
        node[a - 1].append(b - 1)
    counter = [0] * n
    for i in range(q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    queue = deque([0])
    looked[0] = 0
    while queue:
        now = queue.pop()
        for i in node[now]:
            if looked[i]:
                queue.append(i)
                counter[i] += counter[now]
                looked[i] = 0
    print(*counter)

main()
