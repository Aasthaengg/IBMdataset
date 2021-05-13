n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort(); b = 0
for i in range(len(a)):
    if x >= a[i]: x -= a[i]; b += 1
    else: break
else:
    if x > 0: b -= 1
print(b)