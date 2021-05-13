#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ysakamot
#
# Created:     15/12/2018
# Copyright:   (c) ysakamot 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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
    [N] = [int(input_raw[0])]
    print 0
    sys.stdout.flush()

    input_raw = read_func().strip().split()
    s = (input_raw[0])
    if s == "Vacant":
        return
    zero = s

    print N - 1
    sys.stdout.flush()
    input_raw = read_func().strip().split()
    s = (input_raw[0])
    if s == "Vacant":
        return
    L = 0
    R = N - 1
    while 1:
        M = (R + L)/2
        if R - L == 2:
            print M
            sys.stdout.flush()
            input_raw = read_func().strip().split()
            s = (input_raw[0])
            if s == "Vacant":
                return

        if M % 2 == 1:
            M += 1

        print M
        sys.stdout.flush()
        input_raw = read_func().strip().split()
        s = (input_raw[0])
        if s == "Vacant":
            return
        if s == zero:
            L = M
        else:
            R = M


if __name__ == '__main__':
    main()
