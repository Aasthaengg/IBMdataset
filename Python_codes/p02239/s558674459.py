#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def bfs(matrix):
    distances = [-1 for _ in range(len(matrix))]
    queue = [0]
    distances[0] = 0

    while 0 < len(queue):
        node_id = queue.pop(0)  # Dequeue
        distance = distances[node_id]
        for index, candidate in enumerate(matrix[node_id]):
            if candidate == 1 and distances[index] == -1:
                # ???????????¢????¨?????????????????????? node
                queue.append(index)
                distances[index] = distance + 1

    return distances

if __name__ == "__main__":
    # ??????????????????
    # lines = [
    #     "4",
    #     "1 2 2 4",
    #     "2 1 4",
    #     "3 0",
    #     "4 1 3",
    # ]
    lines = sys.stdin.readlines()
    dimension = int(lines[0])
    matrix = [[0 for _ in range(dimension)] for _ in range(dimension)]

    # Set edge info
    for index, line in enumerate(lines[1:]):
        for edge in [int(x) for x in line.strip().split(" ")[2:]]:
            matrix[index][edge - 1] = 1

    distances = bfs(matrix)
    for index, distance in enumerate(distances):
        print("%d %d" % (index + 1, distance))