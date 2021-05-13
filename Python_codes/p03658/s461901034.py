import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    L = [int(l) for l in input().split()]
    L.sort(reverse = True)
    print(sum(L[:K]))

    return 0

if __name__ == "__main__":
    solve()