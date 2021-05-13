n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ret = [0] * n
for i in range(n):
    ret[i] = b[i] - a[i]
ret = sorted(ret)

cnt = 0
for i, val in enumerate(ret):
    if val < 0:
        cnt += abs(val)
        ret[i] = 0
    elif val % 2 == 1:
        cnt += 1
        ret[i] += 1

for i, val in enumerate(ret):
    cnt -= val // 2
if cnt <= 0:
    print("Yes")
else:
    print("No")
