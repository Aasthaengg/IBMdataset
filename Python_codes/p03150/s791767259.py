import sys

def solve():
    input = sys.stdin.readline
    S = input().strip("\n")
    N = len(S)
    w = "keyence"
    for i in range(7):
        if S[:i] == w[:i] and S[N-7+i:] == w[i:]:
            print("YES")
            break
    else: print("NO")

    return 0

if __name__ == "__main__":
    solve()