import sys

def solve():
    input = sys.stdin.readline
    C = [input().strip("\n") for _ in range(3)]
    print(C[0][0] + C[1][1] + C[2][2])

    return 0

if __name__ == "__main__":
    solve()