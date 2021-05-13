# -*-coding: utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    y_dict = {}
    ken_dict = {}
    for i in range(m):
        p_i, y_i = map(int, input().split())
        y_dict[y_i] = []
        y_dict[y_i].append(p_i)

        if not p_i in ken_dict:
            ken_dict[p_i] = []
            ken_dict[p_i].append(y_i)
        else:
            ken_dict[p_i].append(y_i)


    for key in ken_dict.keys():
        ken_dict[key].sort()
        for i,value in enumerate(ken_dict[key]):
            i += 1
            y_dict[value].append(i)
    
    for value in y_dict.values():
        print(str(value[0]).zfill(6) + str(value[1]).zfill(6))
    
    return


if __name__ == '__main__':
    main()