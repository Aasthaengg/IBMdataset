x = list(map(int, input().split()))
insts = input()
for inst in insts:
    if inst == 'N':
        x = [x[1], x[5], x[2], x[3], x[0], x[4]]
    elif inst == 'E':
        x = [x[3], x[1], x[0], x[5], x[4], x[2]]
    elif inst == 'S':
        x = [x[4], x[0], x[2], x[3], x[5], x[1]]
    elif inst == 'W':
        x = [x[2], x[1], x[5], x[0], x[4], x[3]]
print(x[0])