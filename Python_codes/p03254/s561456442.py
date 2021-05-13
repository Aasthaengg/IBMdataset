n, x = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
a.sort()
pos = -1
for i in range(0, n):
    x -= a[i]
    if x < 0:
        pos = i
        break
if pos == -1 and x > 0:
    print(n - 1)
elif x == 0:
    print(n)
else:
    print(pos)