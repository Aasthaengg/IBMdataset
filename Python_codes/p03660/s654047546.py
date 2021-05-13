def main():
    from collections import deque
    import sys
    buf = sys.stdin.buffer
    
    n = int(buf.readline())
    E = map(int, (buf.read().split()))
    edges = [[] for i in range(n)]
    
    for a, b in zip(E, E):
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    
    todo = deque([0, n-1])
    
    colors = [0] * n
    colors[0] = 1
    colors[-1] = 2
    
    while todo:
        node = todo.popleft()
        color = colors[node]
    
        for to in edges[node]:
            if colors[to]:
                continue
            else:
                colors[to] = color
                todo.append(to)
    
    fennec_count = colors.count(1)
    if fennec_count > n // 2:
        print('Fennec ')
    
    else:
        print('Snuke ')


if __name__ == '__main__':
    main()