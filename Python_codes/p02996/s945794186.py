ABs = []

N = int(input())
for _ in range(N):
    ABs.append(tuple(map(int,input().split())))

ABs = sorted(ABs, key=lambda x: x[1])

sum = 0
for A, B in ABs:
    sum += A
    if sum > B:
        print('No')
        exit()
print('Yes')
