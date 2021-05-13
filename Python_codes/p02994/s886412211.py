n, l = map(int, input().split())
apple = []
for i in range(1, n + 1):
    apple.append(i+l-1)
for i in range(400):
    if i in apple:
        apple.remove(i)
        print(sum(apple))
        break
    elif -i in apple:
        apple.remove(-i)
        print(sum(apple))
        break
    else:
        pass