N = int(input())
T = list(map(int, input().split()))
M = int(input())
drinks = [tuple(map(int, input().split())) for _ in range(M)]

sum_T = sum(T)
for problem, time in drinks:
    print(sum_T - T[problem - 1] + time)
