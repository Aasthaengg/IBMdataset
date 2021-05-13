max = -10 ** 9
n = int(input())
min = int(input())
for _ in range(n - 1):
    r = int(input())
    if max < (r - min):
        max = r - min
    if r < min:
        min = r
print(max)