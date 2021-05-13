import sys

def doubleS(s):
    if len(s) % 2 == 1: return False
    L = len(s)
    for i in range(L // 2):
        if s[i] != s[L // 2 + i]:
            return False
    return True

def solve():
    input = sys.stdin.readline
    S = list(input().strip("\n"))
    N = len(S)
    S.pop()
    for i in range(N):
        if doubleS(S):
            print(N - i - 1)
            break
        S.pop()
    else: print(0)

    return 0

if __name__ == "__main__":
    solve()