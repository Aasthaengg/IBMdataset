n = int(input())
a, b = map(int, input().split())
P = list(map(int, input().split()))

x = 0
y = 0
z = 0
for p in P:
    if p <= a:
        x += 1
    elif a+1 <= p <= b:
        y += 1
    else:
        z += 1
print(min([x, y, z]))