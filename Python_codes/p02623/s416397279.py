import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
import numpy as np
def main():
    n, m, k = map(int, input().split())
    a = np.array(readline().split(), np.int64)
    b = np.array(readline().split(), np.int64)
    aa = a.cumsum()
    ba = b.cumsum()
    r = np.searchsorted(ba, k, side='right')    
    for i1, aae in enumerate(aa):
        if k < aae:
            break
        r = max(r, np.searchsorted(ba, k - aae, side='right') + i1 + 1)
    print(r)

if __name__ == '__main__':
    main()