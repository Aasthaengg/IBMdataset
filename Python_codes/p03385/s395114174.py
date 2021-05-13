s = str(input())
apple = []
for i in s:
    apple.append(i)
print("Yes" if len(apple) == len(set(apple)) else "No")