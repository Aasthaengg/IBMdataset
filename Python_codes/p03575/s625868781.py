from typing import List, Tuple


def main():
    n, m = map(int, input().split())
    g = []
    for _ in range(m):
        a, b = map(int, input().split())
        g.append((a, b))
    print(br(n, m, g))


def br(n: int, m: int, g: List[Tuple[int, int]]):
    ret = 0
    for i in range(m):
        v = set()
        w = [1]
        while w:
            now = w.pop()
            v.add(now)
            for j, node in enumerate(g):
                if j == i:
                    continue
                if node[0] == now and node[1] not in v:
                    w.append(node[1])
                elif node[1] == now and node[0] not in v:
                    w.append(node[0])
        if len(v) != n:
            ret += 1
    return ret


if __name__ == '__main__':
    main()
