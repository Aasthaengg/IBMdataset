import sys

input = sys.stdin.readline


def main():
    N, A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    S = input().rstrip()

    if C < D:
        is_ok = True
        for i in range(A, D):
            if S[i:i + 2] == "##":
                is_ok = False
                break
        ans = "Yes" if is_ok else "No"
    else:
        is_ok = True
        for i in range(A, C):
            if S[i:i + 2] == "##":
                is_ok = False
                break
        if not is_ok:
            ans = "No"
        else:
            is_ok = False
            for i in range(B, D + 1):
                if S[i - 1:i + 2] == "...":
                    is_ok = True
                    break
            ans = "Yes" if is_ok else "No"

    print(ans)


if __name__ == "__main__":
    main()
