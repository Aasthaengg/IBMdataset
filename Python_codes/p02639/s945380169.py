x = list(map(int, input().split()))
a = 0
for i in range(5):
    a += x[i]
b = 15 - a
print(b)