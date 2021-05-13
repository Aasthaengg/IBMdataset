# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
解説PDFを読んで書き直した。
ワーシャル-フロイド法を用いる。
"""

def warshall_floyd(c_lsit_list):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                c_lsit_list[j][k] = min(
                    c_lsit_list[j][i] + c_lsit_list[i][k],
                    c_lsit_list[j][k]
                )
    min_c_list = [c_lsit_list[i][1] for i in range(10)]
    return min_c_list

def main():
    H, W = map(int, input().split())
    c_lsit_list = [list(map(int, input().split())) for i in range(10)]
    A_lsit_list = [list(map(int, input().split())) for i in range(H)]

    A_bucket = [0]*10
    for A_list in A_lsit_list:
        for A in A_list:
            if A >= 0:
                A_bucket[A] += 1

    min_c_list = warshall_floyd(c_lsit_list)

    print(sum([A_bucket[i]*min_c_list[i] for i in range(10)]))
    return

if __name__ == "__main__":
    main()

