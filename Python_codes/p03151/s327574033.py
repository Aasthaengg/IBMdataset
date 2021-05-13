import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    if sum(A) < sum(B):
        print(-1)
        return

    plus = []
    totalsa = 0
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            plus.append(A[i] - B[i])
        elif A[i] < B[i]:
            totalsa += B[i] - A[i]
            ans += 1

    plus.sort(reverse=True)

    t = 0
    for i in range(len(plus)):
        if t >= totalsa:
            break
        ans += 1
        t += plus[i]

    print(ans)


if __name__ == '__main__':
    main()
