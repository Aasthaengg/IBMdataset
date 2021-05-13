import sys

input = sys.stdin.readline


def main():
    N = int(input())
    s = [""] * N
    t = [0] * N
    for i in range(N):
        st = input().split()
        s[i] = st[0]
        t[i] = int(st[1])
    X = input().rstrip()

    idx = s.index(X)
    ans = sum(t[idx + 1:])

    print(ans)


if __name__ == "__main__":
    main()
