s = str(input())
apple = []
for i in s:
    apple.append(i)
apple = set(apple)
print("Yes" if len(apple) == 2 else "No")