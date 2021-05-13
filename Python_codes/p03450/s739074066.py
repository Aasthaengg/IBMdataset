import collections
def main():
    N, M = map(int, input().split())
    graph = collections.defaultdict(dict)
    for _ in range(M):
        L, R, D = map(int, input().split())
        graph[L][R] = D
        graph[R][L] = -D

    visited = set()
    used = set()
    for i in range(1, N+1):
        if i not in visited:
            dist = dict()
            dist[i] = 0
            cur = [i]
            visited.add(i)
            while cur:
                temp = []
                for j in cur:
                    for k in graph[j]:
                        if (j, k) not in used and (k, j) not in used:
                            used.add((j, k))
                            used.add((k, j))
                            if k not in dist:
                                dist[k] = dist[j] + graph[j][k]
                                temp.append(k)
                                visited.add(k)
                            elif k in dist:
                                if dist[k] != dist[j] + graph[j][k]:
                                    return "No"
                cur = temp

    return "Yes"

if __name__ == '__main__':
    print(main())