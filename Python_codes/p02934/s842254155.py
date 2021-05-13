import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    ans = 0
    for a in A:
        ans += 1/a
    print(1/ans) 

    return 0

if __name__ == "__main__":
    solve()