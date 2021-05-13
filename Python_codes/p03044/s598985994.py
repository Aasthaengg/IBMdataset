import sys
from collections import deque
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    tree = [[] for _ in range(N)]
    for i in range(N-1):
        u, v, w = map(int, readline().split())
        u, v = u-1, v-1
        tree[u].append((v,w))
        tree[v].append((u,w))
    color = [-1]*N
    color[0]=0

    que = deque([0])
    while que:
        index = que.popleft()
        for next_, weight in tree[index]:
            if color[next_]==-1:
                if weight%2==0:
                    color[next_] = color[index]
                else:
                    color[next_] = color[index]^1
                que.append(next_)
    for c in color:
        print(c)


if __name__ == '__main__':
    main()