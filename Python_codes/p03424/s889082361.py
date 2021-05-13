import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    S = map(str, input().strip("\n"))
    if "Y" in S: print("Four")
    else: print("Three")

    return 0

if __name__ == "__main__":
    solve()