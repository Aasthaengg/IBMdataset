k, s = map(int, input().split())
count = 0

for i in range(k+1):
    for j in range(k+1):

        x = i
        y = j
        z = s - x - y

        if 0 <= z <= k:
            count += 1

print(count)