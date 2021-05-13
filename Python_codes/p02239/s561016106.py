from collections import deque
from typing import List
import sys


def bfs(adj_list: List[List[int]]) -> List[int]:
    n = len(adj_list)
    result: List[int] = [sys.maxsize for _ in range(n)]
    result[0] = 0
    queue: deque = deque()
    queue.append(0)

    while len(queue) > 0:
        cur = queue.popleft()
        for vertex in adj_list[cur]:
            if result[cur] + 1 < result[vertex]:
                result[vertex] = result[cur] + 1
                queue.append(vertex)

    return result


if __name__ == "__main__":
    num_vertices = int(input())
    adj_list: List[List[int]] = [[] for _ in range(num_vertices)]

    for _ in range(num_vertices):
        vertex, num_adjs, *adjs = map(lambda x: int(x), input().split())
        for i in range(num_adjs):
            adj_list[vertex - 1].append(adjs[i] - 1)

    result = bfs(adj_list)

    for i in range(num_vertices):
        if sys.maxsize == result[i]:
            result[i] = -1
        print(f"{i + 1} {result[i]}")

