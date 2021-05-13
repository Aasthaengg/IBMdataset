a, b = map(int, input().split())
# print(a-b+1)

cnt = 0
for i in range(a):
    for j in range(i, a):
        if j - i + 1 == b:
            cnt += 1

print(cnt)
