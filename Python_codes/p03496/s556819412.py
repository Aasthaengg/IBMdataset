n = int(input())
a = list(map(int, input().split()))

count = 0
ans = []
mi = min(a)
ma = max(a)
plus = True
if ma >= 0 and mi <= 0:
    if abs(mi) < ma:
        plus = True
        idx = a.index(ma)+1
    else:
        plus = False
        idx = a.index(mi)+1
    for i in range(1, n+1):
        if i == idx:
            continue
        ans.append([idx, i])
    count += n-1
else:
    plus = ma > 0
if plus:
    for i in range(1, n):
        ans.append([i, i+1])
else:
    for i in range(n-1):
        ans.append([n-i, n-i-1])
print(count+n-1)
for a in ans:
    print("{} {}".format(a[0], a[1]))
