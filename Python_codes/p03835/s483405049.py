k, s = map(int, input().split())

cnt = 0
for x in range(0, k+1):
    for y in range(0, k+1):
        z = s - x - y
        if z < 0 or z > k:
            continue
        cnt +=1
print(cnt)