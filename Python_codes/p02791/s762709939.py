import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    n = int(input())
    a = np.array(read().split(), np.int32)
    mina = np.minimum.accumulate(a)
    r = np.count_nonzero(mina >= a)
    print(r)

if __name__ == '__main__':
    main()