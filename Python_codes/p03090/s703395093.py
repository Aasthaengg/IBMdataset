import sys
from collections import deque
import copy
import math
def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline

def func(root, left, right):
    if right <= left:
        return
    print root, right
    print root, left
    func(right, left + 1, right - 1)

def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [N] = [int(input_raw[0])]
    s = 0
    sum_list = [0 for i in range(N + 1)]
    for i in range(1, N + 1):
        sum_list[i] = sum_list[i - 1] + i
        s += i


    if N % 2 == 0:
        groups = []
        for i in range(1, N/2 + 1):
            groups.append((i, N-i + 1))
        groups = set(groups)
        groups_copy = copy.deepcopy(groups)
        pair = []
        for g1 in groups:
            groups_copy.remove(g1)
            for g2 in groups_copy:
                    for nd1 in g1:
                        for nd2 in g2:
                            if nd1 != 0 and nd2 != 0:
                                pair.append((nd1, nd2))
        print len(pair)
        for i in range(len(pair)):
            print pair[i][0], pair[i][1]
##        left_list = []
##        right_list = []
##
##        for k in range(1, N + 1):
##            left_sum = 0
##            for i in range(k, N + 1):
##                if sum_list[i] - sum_list[i - k] == s / 2:
##                    left_list = set([j for j in range(i - k + 1, i + 1)])
##                    right_list = set([j for j in range(1, N + 1)]) - left_list
##                    print len(left_list) * len(right_list)
##                    for l in left_list:
##                        for r in right_list:
##                            print l, r
##                    return
    else:
        groups = [(N, 0)]
        for i in range(1, N/2 + 1):
            groups.append((i, N-i))
        groups = set(groups)
        groups_copy = copy.deepcopy(groups)
        pair = []
        for g1 in groups:
            groups_copy.remove(g1)
            for g2 in groups_copy:
                    for nd1 in g1:
                        for nd2 in g2:
                            if nd1 != 0 and nd2 != 0:
                                pair.append((nd1, nd2))
        print len(pair)
        for i in range(len(pair)):
            print pair[i][0], pair[i][1]




if __name__ == '__main__':
    main()
