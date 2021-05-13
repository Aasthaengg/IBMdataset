A,B = map(int, input().split())

now = 1
for i in range(100):
    if now >= B:
        print(i)
        break
    now -= 1
    now += A