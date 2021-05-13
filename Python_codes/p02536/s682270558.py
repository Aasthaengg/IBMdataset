import sys

sys.setrecursionlimit(100000)

import numpy as np


def main():
    n_num, m_num = map(int, input().split())
    # road = np.zeros((n_num, n_num), dtype='int32')
    c_map = []
    for _ in range(n_num):
        c_map.append([])
    # print(c_map)

    for _ in range(m_num):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        # road[a-1][b-1] = 1
        c_map[a-1].append(b-1)
        c_map[b-1].append(a-1)
    # print(c_map)

    city_info = np.zeros(n_num, dtype='int32')
    land_city = 0

    def move(a, b):
        if a in c_map[b]:
            return 1
        else:
            return 0

    def recr(c):
        city_info[c] = 1
        for n in c_map[c]:
            if city_info[n] == 0:
                if move(c, n) == 1:
                    recr(n)

    for n in range(n_num):
        if city_info[n] == 0:
            land_city += 1
            recr(n)
    # print(c_map)
    # print(city_info)
    print(land_city - 1)


if __name__ == '__main__':
    main()