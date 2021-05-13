import sys

def solve():
    input = sys.stdin.readline
    S = list(input().strip("\n"))
    if len(S) == len(set(S)): print("yes")
    else: print("no")
    return 0

if __name__ == "__main__":
    solve()