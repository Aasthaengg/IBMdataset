def main():
    import sys
    import numpy as np
    sys.setrecursionlimit(10**6)
    s = input().strip()
    N = len(s)
    p = sum([1 if si == 'p' else 0 for si in s])
    print(N//2-p)

if __name__ == '__main__':
    main()