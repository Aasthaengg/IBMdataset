import sys


def union(parent, rank, i, j):
    i_id = find(parent, i)
    j_id = find(parent, j)

    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1

def find(parent, i):
    v = list()
    while i != parent[i]:
        i = parent[i]
        v.append(i)
    for j in v:
        parent[j] = i
    return i


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n, m = data[0], data[1]
    rank = [0]*(n+1)
    parent = [i for i in range(n+1)]

    for i in range(2,len(data)-1,2):
        union(parent, rank, data[i], data[i+1])

    s = [0]*(n+1)

    # data = data[2:]
    # print(data)

    for i in range(1,n+1):
        s[find(parent,i)] += 1
        # print(i, find(parent, i))

    print(max(s))


if __name__ == '__main__':
    main()
