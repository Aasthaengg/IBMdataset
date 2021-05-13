N, M = map(int, input().split())

min, max = map(int, input().split())

for i in range(1, M):
    L, R = map(int, input().split())
    if L > max or R < min:
        print(0)
        exit()
    elif min < L <= max:
        min = L
    elif min <= R < max:
        max = R
print(max-min+1)
