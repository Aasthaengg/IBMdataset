import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    cand = 10**10
    for i in range(N - K + 1):
        cand = min(cand, h[i + K - 1] - h[i])
    print(cand)





if __name__ == "__main__":
    main()
