import sys

def solve():
    input = sys.stdin.readline
    N, M, C = map(int, input().split())
    B = [int(b) for b in input().split()]
    count = 0
    for i in range(N):
        A = [int(a) for a in input().split()]
        point = C
        for i, a in enumerate(A):
            point += a * B[i]
        if point > 0: count += 1
    print(count)

    return 0

if __name__ == "__main__":
    solve()