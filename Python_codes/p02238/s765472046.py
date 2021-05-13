def main():
    """有向グラフの深さ優先探索
    
    Note: V[i]は頂点iから通じる頂点の集合を意味するが, 
             V[i]: {i}とV[i]: Noneは同値とされている。
    """
    stack = []
    passed_lines = []
    
    n = int(input())
    V = [None]*(n+1)
    D = [None]*(n+1)
    F = [None]*(n+1)
    passed_vertices = set()
    vertices = set(range(1, n+1))
    
    for i in range(1, n+1):
        _, _, *v = map(int, input().split())
        V[i] = set(v)

    i = 1
    time = 1
    stack.append(i)
    passed_vertices.add(i)
    D[i] = time
    while i <= n:
        new_vertices = list(V[i] - passed_vertices - {i})
        new_vertices.sort()
        if new_vertices:
            i = new_vertices[0]
            stack.append(i)
            time += 1
            if D[i] is None:
                D[i] = time
                passed_vertices.add(i)
            continue
        else:
            while stack:
                i = stack.pop()
                time += 1
                if list(V[i] - passed_vertices - {i}):
                    stack.append(i)
                    time -= 1
                    break
                if F[i] is None: 
                    F[i] = time
        if not list(V[i] - passed_vertices - {i}) and not stack:
            rest_vertices = list(vertices-passed_vertices)
            if rest_vertices:
                i = min(rest_vertices)
                stack.append(i)
                time += 1
                if D[i] is None:
                    D[i] = time
                    passed_vertices.add(i)
            else:
                break
    for id, d, f in zip(range(1, n+1), D[1:], F[1:]):
        print("{} {} {}".format(id, d, f))
        
if __name__ == "__main__":
    main()
