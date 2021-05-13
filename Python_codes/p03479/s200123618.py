x, y = map(int, input().split())
for i in range(10**9):
    x *= 2
    if x > y:
        print(i+1)
        break