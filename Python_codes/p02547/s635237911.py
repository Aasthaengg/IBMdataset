n = int(input())
ds1 = []
ds2 = []
for _ in range(n):
    d1,d2 = list(map(int, input().split()))
    ds1.append(d1)
    ds2.append(d2)

matched = [d1 == d2 for d1,d2 in zip(ds1,ds2)]
cnt = 0
for m in matched:
    cnt = cnt+1 if m else 0
    if cnt == 3:
        break

if cnt == 3:
    print('Yes')
else:
    print('No')