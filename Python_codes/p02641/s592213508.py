x, n = map(int, input().split())
l = list(map(int, input().split()))

if x not in l:
    print(x)
    exit()

x_a = x
for i in range(100):
    x -= 1
    x_a += 1
    if x not in l:
        print(x)
        exit()
    if x_a not in l:
        print(x_a)
        exit()