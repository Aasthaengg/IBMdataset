from collections import deque
import sys
read = sys.stdin.read
readline = sys.stdin.readline


def main():
    n = int(readline())

    E = [[]]
    for _ in range(n):
        u,k,*v = map(int, readline().split())
        E.append(v)

    d = [-1] * (n+1)
    
    queue = deque([1])
    d[1] = 0
    while queue:
        v = queue.popleft()
        for e in E[v]:
            if d[e] == -1:
                d[e] = d[v] + 1
                queue.append(e)

    for i in range(1, n+1):
        print(i, d[i])


if __name__ == "__main__":
    main()
