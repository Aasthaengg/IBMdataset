N = int(input())
T = list(map(int, input().split()))
M = int(input())
P_and_T = [list(map(int, input().split())) for _ in range(M)]
t_sum = sum(T)
for p, x in P_and_T:
    print(t_sum - T[p-1] + x)
