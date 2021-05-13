import collections
def main():

    N = int(input())
    graph = collections.defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cur1 = [1]
    cur2 = [N]
    visited1 = {1}
    visited2 = {N}

    while cur1 or cur2:
        temp1, temp2 = [], []
        for a in cur1:
            for b in graph[a]:
                if b not in visited1 and b not in visited2:
                    temp1.append(b)
                    visited1.add(b)
        cur1 = temp1

        for a in cur2:
            for b in graph[a]:
                if b not in visited1 and b not in visited2:
                    temp2.append(b)
                    visited2.add(b)
        cur2 = temp2

    if len(visited1) > len(visited2):
        return "Fennec"
    return "Snuke"


if __name__ == '__main__':
    print(main())