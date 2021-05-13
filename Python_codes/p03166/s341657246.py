import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

longs = []
edges = {}
def graph_DP(node_to):
    global longs
    if longs[node_to] != -1:
        return longs[node_to]
    else:
        nodes_next = edges[node_to]
        if not nodes_next:
            longs[node_to] = 0
            return 0
        else:
            long_max_t = 0
            for node_next in nodes_next:
                if longs[node_next] != -1:
                    long_max_t = max(long_max_t, longs[node_next] + 1)
                else:
                    long_max_t = max(long_max_t, graph_DP(node_next) + 1)
            longs[node_to] = long_max_t
            return long_max_t

def main():
    global longs, edges
    n, m = map(int, input().split())
    edges = {e:set() for e in range(1, n + 1)}
    for _ in range(m):
        s, g = map(int, input().split())
        edges[s].add(g)
    longs = [-1] * (n + 1)

    for i1 in range(1, n + 1):
        if longs[i1] == -1:
            graph_DP(i1)
    print(max(longs))

if __name__ == '__main__':
    main()