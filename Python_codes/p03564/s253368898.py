
n = int(input())
k = int(input())
x = 1

for i in range(n):
    if x * 2 >= x + k:
        x = x + k
    else:
        x *= 2

print(x)
