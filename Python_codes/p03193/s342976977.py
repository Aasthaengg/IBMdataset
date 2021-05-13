n, h, w = map(int, input().split())
a = list()
b = list()
for i in range (n):
    tempa, tempb = map(int, input().split())
    a.append(tempa)
    b.append(tempb)


ans = 0
for i in range(n):
    if (int(a[i]) >= h) and (int(b[i]) >= w):
        ans += 1

print(int(ans))