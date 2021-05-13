n = int(input())
a = list(map(int, input().split()))

h = a[0]
step = 0
for i in range(1,n):
    if a[i] > h:
        h = a[i]
    elif a[i] < h:
        d = h - a[i]
        step += d

print(step)