import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    a = np.fromstring(read(), np.int64, sep=' ')[1:]
    a = a[a % 2 == 0]
    if np.all((a % 3 == 0) | (a % 5 == 0)):
        print('APPROVED')
    else:
        print('DENIED')

if __name__ == '__main__':
    main()
