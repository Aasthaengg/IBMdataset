n = int(input())
k = int(input())
x = 1

for i in range(1, n+1):
    if x * 2 < x + k:
        x = x * 2
    else:
        x = x + k
print(x)
