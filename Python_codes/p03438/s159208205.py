import math

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt1, cnt2 = 0, 0
for i in range(N):
    if a[i] > b[i]:
        cnt1 += a[i] - b[i]
    elif a[i] < b[i]:
        cnt2 += math.ceil((b[i]-a[i])/2)

cnt = sum(b) - sum(a)
if cnt1 <= cnt and cnt2 <= cnt:
    print('Yes')
else:
    print('No')