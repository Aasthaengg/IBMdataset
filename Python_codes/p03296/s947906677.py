n = int(input())
a = list(map(int, input().split()))
a.insert(0, -1)
a.append(-1)
m = []
cnt = 0
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        if cnt != 0:
            m.append(cnt)
        cnt = 1
    else:
        cnt += 1
total = 0
for i in m:
    total += i // 2
print(total)
