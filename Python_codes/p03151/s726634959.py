n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x, y = [], []
for i in range(n):
    if a[i] > b[i]:
        x.append(a[i] - b[i])
    else:
        y.append(b[i] - a[i])
ans = -1
if sum(x) >= sum(y):
    if sum(y) == 0:
        ans = 0
    else:
       dif = sum(x) - sum(y)
       x = sorted(x)
       index = 0
       total = 0
       while total + x[index] <= dif:
           total += x[index]
           index += 1
       ans = n - index
print(ans)
