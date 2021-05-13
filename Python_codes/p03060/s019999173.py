# 初期入力
import numpy as np
import sys
input = sys.stdin.readline
N = int(input())
V = np.array(list(map(int, input().split())))
C = np.array(list(map(int, input().split())))

#どの宝石を選ぶか全探索
v_c_sum=0
for i in range(N):
    if 0 < V[i] -C[i]:
        v_c_sum +=V[i] - C[i]
print(v_c_sum)