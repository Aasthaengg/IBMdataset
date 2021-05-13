#!/usr/bin/env python3

import heapq

P = list(map(int, input().split()))

_list = heapq.nsmallest(2, P)

print(_list[0] + _list[1])