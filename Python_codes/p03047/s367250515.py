#! usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
import heapq
import math
import bisect


def main():
    N, K = map(int, input().split())
    print(N-K+1)


if __name__ == '__main__':
    main()
