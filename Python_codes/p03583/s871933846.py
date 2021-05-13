import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from numba import njit

def main():
    N = int(input())
    @njit
    def solve(N):
        for h in range(1, 3501):
            for n in range(1, 3501):
                shisu = h * N * n
                bosu = n * (h * 4 - N) - h * N
                if bosu >= 1 and not (shisu / bosu) % 1:
                    return h, n , int((h * N * n) / (n * (h * 4 - N) - h * N))
    r = solve(N)
    print(*r , sep=' ')

if __name__ == '__main__':
    main()