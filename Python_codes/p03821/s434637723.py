import sys

def solve():
    input  = sys.stdin.readline
    N = int(input())
    array = [[int(a) for a in input().split()] for _ in range(N)]
    count = 0
    for i in reversed(range(N)):
        a, b = array[i]
        if (a + count) % b == 0: continue
        else: count += b - ((a + count) % b)
    print(count)

    return 0

if __name__ == "__main__":
    solve()