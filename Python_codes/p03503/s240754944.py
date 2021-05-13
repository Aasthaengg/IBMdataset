import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    F = [[] for _ in range(n)]
    for w in range(n):
        l = list(map(int, input().split()))
        for i in range(5):
            F[w].append(l[i * 2: i * 2 + 2])
    P = [list(map(int, input().split())) for _ in range(n)]

    ans = -10**10
    for case in range(1, 1 << 10):
        profit = 0
        for i in range(n):
            c = 0
            for t in range(10):
                if F[i][t // 2][t % 2] and case & (1 << t): c += 1
            profit += P[i][c]
        ans = max(ans, profit)
    print(ans)



if __name__ == "__main__":
    main()
