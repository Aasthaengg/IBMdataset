x = int(input())
n = 1
d = 0
while d < x:
    d = n * (n + 1) // 2
    n += 1
print(n - 1)
