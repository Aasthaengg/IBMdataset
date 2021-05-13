N = int(input())
array = [list(map(int, input().split())) for i in range(N)]
for line in array:
    line.append(line[0] - line[1])
    line.append(line[0] + line[1])
array = sorted(array, key=lambda x: x[3])

count = 0
max_r = -float('inf')
for i in range(N):
    current = array[i]
    if current[2] >= max_r:
        count += 1
        max_r = current[3]
print(count)
