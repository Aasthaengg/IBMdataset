x = int(input())
a = 0
for i in range(1, 1001):
    for j in range(2, 20):
        if i**j <= x:
            a = max(i**j, a)

print(a)