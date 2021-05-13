import sys
input = sys.stdin.readline
N, C, K = [int(x) for x in input().split()]
T = [int(input()) for _ in range(N)]
T.sort()
depart = T[0] + K  # 出発時刻
passenger = 0  # 乗客数
bus = 1
for i in range(N):
    if passenger >= C or depart < T[i]:  # すでに満員または待ち時間オーバー
        bus += 1
        passenger = 1
        depart = T[i] + K
    else:
        passenger += 1

print(bus)