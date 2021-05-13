import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import combinations
def main():
    def divisor(n):
        i = 1
        t = []
        while i * i <= n:
            if n % i == 0:
                t.append(i)
                t.append(n // i)
            i += 1
        return len(set(t))

    n = int(input())
    r = 0
    for i1 in range(1, n + 1, 2):
        r += 8 == divisor(i1)
    print(r)

if __name__ == '__main__':
    main()
