x, y = map(int, input().split())
i = 0
while 2**i <= y//x:
    i += 1
print(i)