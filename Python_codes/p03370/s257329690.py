import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, X = map(int, input().split())
    M = [int(input()) for _ in range(N)]
    X -= sum(M)
    M.sort()
    print(N + X // M[0])

if __name__ == "__main__":
    main()
