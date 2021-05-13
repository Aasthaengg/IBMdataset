# -*- coding:utf-8 -*-
import sys


def liner_search(data, targets):
    cnt = 0
    for num in targets:
        if num in data:
            cnt += 1
    return cnt


if __name__ == "__main__":
    data = [val.split() for val in sys.stdin.read().splitlines()]
    print(liner_search(data[1], data[3]))