num = int(input())
a = list(map(int, input().split()))
k = 1
x = y = 0
c = a[0]
for i in a[1:]:
    if c < i:
        x = 1
    elif c > i:
        y = 1
    if x == 1 and y == 1:
        k += 1
        x = y = 0
    c = i
print(k)