import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    N, H = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort(reverse=True)

    throw = []
    for i in range(N):
        if B[i] > A[-1]:
            throw.append(B[i])
    # print(throw)
    throw = throw[::-1]

    ans = 0

    while H > 0:
        if throw:
            H -= throw.pop()
            ans += 1
        else:
            need_try = (H + A[-1] - 1) // A[-1]
            ans += need_try
            break

    print(ans)


if __name__ == "__main__":
    main()
