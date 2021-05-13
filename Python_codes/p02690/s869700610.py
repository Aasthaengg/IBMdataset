import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    x = int(input())
    n5 = np.array([i**5 for i in range(-201, 201)])
    diff = np.subtract.outer(n5, n5)
    r = np.where(diff == x)
    # assert (r[0][0] - 201)**5 - (r[1][0] - 201)**5 == x
    print(r[0][0]-201, r[1][0]-201)

if __name__ == '__main__':
    main()
