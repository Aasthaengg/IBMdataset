import sys


def input():
    return sys.stdin.readline()[:-1]


N, C, K = map(int, input().split())
T = [0]*N
for i in range(N):
    T[i] = int(input())

T.sort()

ans = 0
bus_time = -1
bus_num = 0
for i in range(N):
    # 新しいバス
    if bus_time == -1:
        bus_time = T[i]
        bus_num = 1
        ans += 1
    elif T[i] <= bus_time+K and bus_num <= C:
        bus_num += 1
    else:
        bus_time = T[i]
        bus_num = 1
        ans += 1

    if bus_num == C:
        bus_time = -1
        bus_num = 0
print(ans)
