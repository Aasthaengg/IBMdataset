import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    nums = np.array(read().split(), np.int64)
    a = nums[:9]

    for x in nums[10:]:
        a[a == x] = 0
    pos = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for pose in pos:
        if a[pose[0]] == a[pose[1]] == a[pose[2]] == 0:
            print('Yes')
            sys.exit()
    print('No')

if __name__ == '__main__':
    main()
