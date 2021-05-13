X = int(input())

cnt = 0
dist = 0

while X > dist:
    dist += (cnt + 1)
    cnt += 1
print(cnt)