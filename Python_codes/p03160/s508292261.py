def i_input(): return int(input())


def i_map(): return map(int, input().split())


def i_list(): return list(i_map())


n = i_input()
h = i_list()
cost = [0] * n

for i in range(n):
    if i == 0:
        cost[i] = 0
    elif i == 1:
        cost[i] = abs(h[i] - h[i - 1])
    else:
        h_1 = abs(h[i] - h[i - 1])
        h_2 = abs(h[i] - h[i - 2])
        cost[i] = min(cost[i - 1] + h_1, cost[i - 2] + h_2)
print(cost[n - 1])
