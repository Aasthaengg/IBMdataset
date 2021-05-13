import sys
from itertools import combinations
def input(): return sys.stdin.readline().strip()


def main():
    H, W, D = map(int, input().split())
    place = {}
    for i in range(H):
        A = list(map(int, input().split()))
        for j in range(W):
            place[A[j] - 1] = (i, j)
    magic = [0] * (H * W)
    for n in range(D):
        val = n
        x, y = place[val]
        while val + D < H * W:
            nx, ny = place[val + D]
            magic[val + D] = abs(nx - x) + abs(ny - y) + magic[val]
            val += D
            x, y = nx, ny
    #print(magic)

    Q = int(input())
    ans = 0
    for _ in range(Q):
        l, r = map(int, input().split())
        print(magic[r-1] - magic[l-1])


if __name__ == "__main__":
    main()
