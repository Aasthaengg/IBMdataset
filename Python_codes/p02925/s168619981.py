import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))
from collections import defaultdict, deque

edges = defaultdict(lambda: [])
used = set()
d = defaultdict(lambda: 0)


def dfs(i):
    if i in used:
        return d[i]
    used.add(i)
    ret = -1
    for v in edges[i]:
        tmp = dfs(v)
        ret = max(ret, tmp)
    d[i] = ret + 1
    return ret+1

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    h = {}
    for i, al in enumerate(a):
        for pa, ta in zip(al, al[1:]):
            pa, ta = pa-1, ta-1
            edges[1000*min(i, pa)+max(i, pa)].append(1000*min(i, ta)+max(i, ta))
            if 1000*min(i, pa)+max(i, pa) not in h:
                h[1000*min(i, pa)+max(i, pa)] = 0
            if 1000*min(i, ta)+max(i, ta) not in h:
                h[1000*min(i, ta)+max(i, ta)] = 1
            else:
                h[1000*min(i, ta)+max(i, ta)] += 1
    
    deq = deque([])
    for k, v in h.items():
        if v == 0:
            deq.append(k)
    
    ans = 0
    while deq:
        u = deq.popleft()
        for v in edges[u]:
            h[v] -= 1
            if h[v] == 0:
                deq.append(v)
        ans += 1
    
    if ans != n*(n-1) // 2:
        print(-1)
    else:
        length = 0
        for k, _ in edges.items():
            tmp = dfs(k)
            length = max(length, tmp)
        print(length + 1)


if __name__ == '__main__':
    main()
