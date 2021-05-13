import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from numba import njit
def main():
    @njit
    def solve(n):
        r = 0
        for i1 in range(1, n + 1):
            for i2 in range(i1, n + 1, i1):
                r += i2
        return r
    no = int(input())
    print(solve(no))
if __name__ == '__main__':
    main()
