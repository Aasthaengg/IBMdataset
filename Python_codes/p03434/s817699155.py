n = int(input())
a = list(map(int, input().split()))
a.sort()
x = 0
y = 0
for i in range(len(a)):
    b = a.pop()
    if i % 2 == 0:
        x += b
    else:
        y += b
print(x - y)