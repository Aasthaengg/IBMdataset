A, B = map(int, input().split())
for i in range(500000):
    a = i * 8 // 100
    b = i // 10
    if (a, b) == (A, B):
        print(i)
        exit()
print(-1)
