A, B = map(int, input().split(' '))
rst = -1
for i in range(1, 100000):
    if i * 8 // 100 == A and i * 10 // 100 == B:
        rst = i
        break
print(rst)