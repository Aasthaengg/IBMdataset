s = str(input())
apple = []
for i in s:
    apple.append(i)
print("yes" if len(apple) == len(set(apple)) else "no")