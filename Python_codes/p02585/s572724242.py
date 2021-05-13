import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())
    P = [int(s) - 1 for s in readline().split()]
    C = list(map(int, readline().split()))

    ans = -INF
    for i in range(N):
        score = []
        total = 0
        x = i
        while True:
            x = P[x]
            score.append(C[x])
            total += C[x]
            if x == i:
                break

        l = len(score)
        csum = 0
        for i in range(l):
            if i + 1 > K:
                break
            csum += score[i]
            res = csum
            if total > 0:
                res += (K - (i + 1)) // l * total

            if ans < res:
                ans = res

    print(ans)
    return


if __name__ == '__main__':
    main()
