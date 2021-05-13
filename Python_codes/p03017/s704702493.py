import sys
input = sys.stdin.readline  # NOQA


def main():
    N, A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    S = input().rstrip()

    can_jump_R = True  # '##'
    can_jump_B = False  # '...'
    for i in range(A + 1, N - 1):
        if S[i] == S[i+1] == "#":
            if A < i < C or B < i < D:
                can_jump_R = False
        if S[i-1] == S[i] == S[i+1] == ".":
            if B <= i < C and i-1 != D:
                can_jump_B = True

    if C < D:
        if can_jump_R:
            ans = "Yes"
        else:
            ans = "No"
    else:
        if can_jump_R and can_jump_B:
            ans = "Yes"
        else:
            ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
