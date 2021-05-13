N, T = map(int, input().split())

Times = list(input().split())
time = 0

for i in range(N - 1):
    if int(Times[i]) + T <= int(Times[i + 1]):
        time += T
    else:
        time = time + (int(Times[i + 1]) - int(Times[i]))

print(time + T)
