import sys


def read():
    return sys.stdin.buffer.readline().rstrip()


def main():
    n, m = map(int, read().split())
    al = [[] for _ in range(n)]
    for _ in range(m):
        a, b = [int(i) - 1 for i in read().split()]
        al[a].append(b)
        al[b].append(a)
    cnt = 0
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        todo = [i]
        while todo:
            p = todo.pop()
            if p in seen:
                continue
            seen.add(p)
            todo += al[p]
        cnt += 1
    print(cnt - 1)


if __name__ == '__main__':
    main()
