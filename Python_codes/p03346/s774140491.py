import sys
from collections import deque
import copy

from math import *

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
    N = int(input_raw[0])
    Q = [0 for i in range(N + 1)]
    count = 0
    for i in range(N):
        input_raw = read_func().strip().split()
        Q[int(input_raw[0])] = i

    count = 1
    max_count = 0
    for i in range(1, N):
        if Q[i] < Q[i + 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    if max_count == 0:
        max_count = N

    print N - max_count


if __name__ == '__main__':
    main()
