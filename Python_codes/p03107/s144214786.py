s = str(input())
apple = []
for i in s:
    apple.append(i)
a = apple.count("1")
b = apple.count("0")
print(2 * (min(a, b)))