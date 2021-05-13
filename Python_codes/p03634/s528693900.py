from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
def main():
    n = int(input())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1
        G[a].append([b, c])
        G[b].append([a, c])
    q, k = list(map(int, input().split()))
    k -= 1
    stack = deque([k, ])
    ans = [-1] * n
    ans[k] = 0
    while stack:
        x = stack.popleft()
        for (dx, l) in G[x]:
            if ans[dx] == -1:
                ans[dx] = ans[x] + l
                stack.appendleft(dx)
    for _ in range(q):
        x, y = list(map(lambda x: int(x) - 1, input().split()))
        print(ans[x] + ans[y])

if __name__ == '__main__':
    main()
