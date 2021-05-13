N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
for i in range(len(a)):
    if x - a[i] >= 0:
        x -= a[i]
        count += 1
    else:
        break
if count == N and x  > 0:
    print(count - 1)
else:
    print(count)