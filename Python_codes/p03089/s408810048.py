import sys

input = sys.stdin.readline


def main():
    N = int(input())
    B = list(map(int, input().split()))

    is_ok = True
    for i, b in enumerate(B, 1):
        if i < b:
            is_ok = False
    if not is_ok:
        print(-1)
        exit()

    ans = []
    for _ in range(N):
        for i in reversed(range(len(B))):
            if B[i] == i + 1:
                break
        ans.append(B[i])
        del B[i]

    ans = ans[::-1]
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
