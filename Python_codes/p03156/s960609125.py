N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
x = 0
y = 0
z = 0

for i in P:
    if i <= A:
        x += 1
    elif i <= B:
        y += 1
    else:
        z += 1
print(min(x, y, z))
