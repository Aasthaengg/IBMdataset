import sys


def input():
    return sys.stdin.readline()[:-1]


N, C, K = map(int, input().split())
T = [0]*N
for i in range(N):
    T[i] = int(input())
T.sort()

ans = 1
bus_time = T[0]
bus_num = 0
for i in range(N):
    if T[i] <= bus_time+K and bus_num < C:
        # 止まっているバスに乗る
        bus_num += 1
    else:
        # 新しいバスが必要
        bus_time = T[i]
        bus_num = 1
        ans += 1

print(ans)
