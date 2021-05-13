n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
am = 0
bm = 0
for i in range(n):
    if a[i] == b[i]:
        continue
    elif a[i] > b[i]:
        bm += a[i] - b[i]
    else:
        am += (b[i] - a[i] + 1) // 2
        if (b[i] - a[i]) % 2:
            bm += 1
if am - bm >= 0:
    print('Yes')
else:
    print('No')
