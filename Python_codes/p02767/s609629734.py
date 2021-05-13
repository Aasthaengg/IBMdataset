import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    n = int(input())
    p = np.array(read().split(), np.int32)
    r = float('inf')
    for i1 in range(101):
        r = min(r, sum((p - i1)**2))
    print(r)

if __name__ == '__main__':
    main()