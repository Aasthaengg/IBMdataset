import sys
readline = sys.stdin.readline
from math import floor, ceil

def main():
    N = int(readline())
    inp = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    scr_t, scr_a = 1, 1
    for t, a in inp:
        # n = max(ceil(scr_t/t), ceil(scr_a/a))
        n = max((scr_t//t)+(scr_t%t!=0), (scr_a//a)+(scr_a%a!=0))
        scr_t = n * t
        scr_a = n * a

    print(scr_t + scr_a)

if __name__ == '__main__':
    main()