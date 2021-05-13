import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]

f_inf = float("inf") # sys.maxsize

N, M, P = map(int, input().split())
ABC_d = {}
for m in range(M):
    A, B, C = map(int, input().split())
    if A in ABC_d:
        ABC_d[A].append((B, C - P))
    else:
        ABC_d[A] = [(B, C - P)]

cost = [-f_inf] * N
cost[0] = 0

max_num_sum = (N * (N + 1)) // 2

def solve(pos, cnt, num_sum):
    global cost

    if not(pos in ABC_d): return
    if cnt > N or num_sum > max_num_sum:
        cost[pos-1] = f_inf;

    for B, C in ABC_d[pos]:
        if cost[B - 1] == f_inf or cost[B - 1] >= cost[pos - 1] + C:
            pass
        elif cost[B - 1] < cost[pos - 1] + C:
            cost[B - 1] = cost[pos - 1] + C
            solve(B, cnt + 1, num_sum + B)

solve(1, 1, 1)

if (cost[-1] == f_inf):
    print (-1)
else:
    print (max(0, int(cost[-1])))
