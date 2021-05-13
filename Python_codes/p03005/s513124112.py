import sys
from collections import deque
import copy
import math
def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline



def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [N, K] = [int(input_raw[0]), int(input_raw[1])]
    if (K == 1):
        print 0
    else:
        print (N - (K - 1)- 1)


if __name__ == '__main__':
    main()
