import sys

def solve():
    input = sys.stdin.readline
    C = [int(i) for i in input().split()]
    C.sort()
    if C[0] + C[1] == C[2]: print("Yes")
    else: print("No")

    return 0

if __name__ == "__main__":
    solve()