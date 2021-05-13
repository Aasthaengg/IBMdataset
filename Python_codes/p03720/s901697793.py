import sys
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    path = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        path[a - 1] += 1
        path[b - 1] += 1
    for p in path: print(p)


if __name__ == "__main__":
    main()
