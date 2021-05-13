x, y = map(int, input().split())
if x == y or y == 1 or x % y == 0:
    print(-1)
    exit()
for i in range(1, 10**5):
    if x * i % y != 0:
        print(x*i)
        exit()
