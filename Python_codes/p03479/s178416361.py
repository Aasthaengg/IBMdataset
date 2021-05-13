x, y = map(int, input().split())
div = y // x
i = 0
while div >= pow(2, i):
    i += 1
print(i)