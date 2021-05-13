n = int(input())
a = []
ans = 0
flag = True
for i in range(n):
    A = int(input())
    a.append(A)
next = 0
for i in range(n-1,-1,-1):
    if next - a[i] >= 2:
        flag = False
        break
    if a[i] == 0:
        next = 0
        continue
    if next - a[i] == 1:
        next = a[i]
        continue
    next = a[i]
    ans += a[i]
if a[0] != 0:
    flag = False
if flag:
    print(ans)
else:
    print(-1)
