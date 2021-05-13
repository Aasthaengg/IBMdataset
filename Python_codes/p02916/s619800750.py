n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

point = 0

prev = -2

for i in range(n):
    food = a[i]-1
    point += b[food]
    if food == prev + 1:
        point += c[prev]
    prev = food

print(point)
