import sys
def input(): return sys.stdin.readline().strip()


def main():
    n, k = map(int, input().split())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    print(sum(L[:k]))

if __name__ == "__main__":
    main()
