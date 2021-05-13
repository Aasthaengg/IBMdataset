import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import Counter
def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    suma = sum(a)
    aa = Counter(a)
    q = int(input())
    m = map(int, read().split())
    for b, c in zip(m, m):
        kosu = aa[b]
        sa = c - b
        suma += sa * kosu
        print(suma)
        aa[b] = 0
        aa[c] += kosu

if __name__ == '__main__':
    main()
