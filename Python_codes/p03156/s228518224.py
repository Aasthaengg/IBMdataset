n = int(input())
a, b = map(int, input().split())
l = list(map(int, input().split()))
x = 0
y = 0
z = 0
for i in range(n):
    if l[i] <= a:
        x += 1
    elif a + 1 <= l[i] <= b:
        y += 1
    elif b + 1 <= l[i]:
        z += 1
print(min(x,y,z))