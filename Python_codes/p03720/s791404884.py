# -*- coding: utf-8 -*-

N, M = map(int, input().split())

road_count_list = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    road_count_list[a - 1] = road_count_list[a - 1] + 1
    road_count_list[b - 1] = road_count_list[b - 1] + 1

print(*road_count_list, sep='\n')