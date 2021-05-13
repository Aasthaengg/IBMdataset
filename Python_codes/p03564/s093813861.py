n = int(input())
k = int(input())
mini = 10**10

for i in range(2 ** n):
    x = 1
    for j in range(n):
        if ((i >> j) & 1):
            x *= 2
        else:
            x += k
    mini = min(mini,x)
print(mini)