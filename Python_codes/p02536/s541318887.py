def root(list_parent, x):
    if(list_parent[x] == x):
        return x
    else:
        list_parent[x] = root(list_parent, list_parent[x])
        return list_parent[x]

def unite(list_parent, x, y):
    x = root(list_parent, x)
    y = root(list_parent, y)

    if(x == y):
        return list_parent

    if x > y:
        list_parent[y] = x
    else:
        list_parent[x] = y

    return list_parent

def main():
    N, M = map(int, input().split())

    list_parent = []
    for i in range(N):
        list_parent.append(i)

    for i in range(M):
        A, B = map(int, input().split())
        list_parent = unite(list_parent, A-1, B-1)

    set_root = set()
    for i in list_parent:
        root_i = root(list_parent, i)
        if root_i not in set_root:
            set_root.add(root_i)

    print(len(set_root) - 1)

if __name__ == "__main__":
    main()