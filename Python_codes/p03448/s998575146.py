c = [0] * 3
for i in range(3):
    c[i] = int(input())
x = int(input())
cnt = 0
for i in range(c[0] + 1):
    for j in range(c[1] + 1):
        req = x - (i * 500 + j * 100)
        if req >= 0 and req % 50 == 0 and req // 50 <= c[2]:
            cnt += 1
print(cnt)
