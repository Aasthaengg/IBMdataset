import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))


def main():
    n, m, p = map(int, input().split())

    nodes = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        nodes.append((a - 1, b - 1, -(c - p)))
    
    d = [float("inf") for _ in range(n)]
    pre = [-1 for _ in range(n)]
    d[0] = 0
    for _ in range(n):
        for nod in nodes:
            if d[nod[1]] > d[nod[0]] + nod[2]:
                d[nod[1]] = d[nod[0]] + nod[2]
                pre[nod[1]] = nod[0]

    for i, nod in enumerate(nodes):
        if d[nod[1]] > d[nod[0]] + nod[2]:
            nodes[i] = (nod[0], nod[1], -float('inf'))
    
    d = [float("inf") for _ in range(n)]
    pre = [-1 for _ in range(n)]
    d[0] = 0
    for _ in range(n):
        for nod in nodes:
            if d[nod[1]] > d[nod[0]] + nod[2]:
                d[nod[1]] = d[nod[0]] + nod[2]
                pre[nod[1]] = nod[0]

    path = set()
    fr = n - 1
    while pre[fr] != -1:
        if fr in path:
            break
        path.add(pre[fr])
        fr = pre[fr]

    for nod in nodes:
        if d[nod[1]] > d[nod[0]] + nod[2]:
            if nod[0] in path:
                print(-1)
                return

    if d[n - 1] == -float('inf'):
        print(-1)
        return 

    if d[n - 1] > 0:
        print(0)
    else:
        print(-d[n - 1])
    

if __name__ == '__main__':
    main()
