N = int(input())
T = tuple(map(int, input().split()))
M = int(input())
drinks = [list(map(int, input().split())) for _ in range(M)]
for drink in drinks:
    total_time = sum(T) - (T[drink[0]-1] - drink[1])
    print(total_time)
