#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque

UNVISITED, VISITED_IN_QUEUE, POPPED_OUT = 0, 1, 2


def generate_adj_matrix(v_info):
    for v_detail in v_info:
        v_adj_list = v_detail[2:]
        # assert len(v_adj_list) == int(v_detail[1])
        for each in v_adj_list:
            init_adj_matrix[int(v_detail[0]) - 1][int(each) - 1] = 1
    return init_adj_matrix


def graph_bfs(v_init):
    vertices_status_list[v_init] = VISITED_IN_QUEUE
    vertices_distance_list[v_init] = 0
    vertices_visit_queue.appendleft(v_init)

    while vertices_visit_queue:
        current_vertex = vertices_visit_queue.popleft()
        for v in range(1, vertices_num + 1):
            if adj_matrix[current_vertex - 1][v - 1] and vertices_status_list[v] is UNVISITED:
                vertices_status_list[v] = VISITED_IN_QUEUE
                vertices_distance_list[v] = vertices_distance_list[current_vertex] + 1
                vertices_visit_queue.append(v)
        vertices_status_list[current_vertex] = POPPED_OUT
    return vertices_distance_list


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices_num = int(_input[0])
    vertices_info = list(map(lambda x: x.split(), _input[1:]))
    init_adj_matrix = [[0] * vertices_num for _ in range(vertices_num)]
    # assert len(vertex_info) == vertex_num

    # config length = (vertex_num + 1)
    vertices_visit_queue = deque()
    vertices_status_list = [UNVISITED] * vertices_num
    vertices_status_list.insert(0, -1)
    vertices_distance_list = [-1] * (vertices_num + 1)

    adj_matrix = generate_adj_matrix(vertices_info)
    ans = graph_bfs(v_init=1)
    for j in range(vertices_num):
        print(j + 1, ans[j + 1])