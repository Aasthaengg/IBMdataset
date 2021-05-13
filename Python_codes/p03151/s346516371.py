n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pu = []
ma = []
for x, y in zip(a, b):
    if x - y < 0:
        ma.append(x - y)
    else:
        pu.append(x - y)
if sum(pu) + sum(ma) < 0:
    print(-1)
else:
    cnt = len(ma)
    ma_sum = sum(ma)
    pu.sort(reverse = True)
    while ma_sum < 0:
        cnt += 1
        ma_sum += pu.pop(0)
    print(cnt)