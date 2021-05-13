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
    [N, A, B] = [int(input_raw[0]), int(input_raw[1]), int(input_raw[2])]
    if (B- A - 1) % 2 == 1:
        print "Alice"
    else:
        print "Borys"


if __name__ == '__main__':
    main()
