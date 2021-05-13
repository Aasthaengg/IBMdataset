a, b, c = map(int, input().split())
for i in range(0, 101):
    if a > b or i == c:
        print(i)
        break
    b = b - a