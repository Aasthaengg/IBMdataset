import sys
def input(): return sys.stdin.readline().strip()


def main():
    D, N = map(int, input().split())
    cnt = 0
    n = 1
    while cnt < N:
        if n % (100**D) == 0 and n % (100**(D + 1)) != 0: cnt += 1
        n += 1
        if cnt == N: print(n - 1)

if __name__ == "__main__":
    main()
