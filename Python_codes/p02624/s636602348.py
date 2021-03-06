import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numba
def main():
    @numba.njit('(i8,)', cache=True)
    def solve(n):
        r = 0
        for i1 in range(1, n + 1):
            y = n // i1
            r += y * (y + 1) // 2 * i1
        return r
    no = int(input())
    print(solve(no))

if __name__ == '__main__':
    main()