import sys
input = sys.stdin.readline


def main():
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))

    D.sort()
    T.sort()

    ans = "YES"
    d = 0
    for t in T:
        found = False
        for i in range(d, N):
            if D[i] == t:
                found = True
                d = i + 1
                break
        if not found:
            ans = "NO"
            break
    print(ans)


if __name__ == "__main__":
    main()
