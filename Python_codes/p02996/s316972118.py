ABs = []

N = int(input())
for i in range(N):
    ABs.append(list(map(int,input().split())))

ABs = sorted(ABs, key=lambda x: x[1])

sum = 0
for pair in ABs:
    sum += pair[0]
    if sum > pair[1]:
        print('No')
        exit()
print('Yes')