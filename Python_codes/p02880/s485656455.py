# 81
N = int(input())
ct = 0
for i in range(10):
    for j in range(10):
        if i * j == N:
            ct += 1
if ct == 0:
    print('No')
else:
    print('Yes')
