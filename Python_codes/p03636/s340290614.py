s = str(input())

apple = []
for i in s:
    apple.append(i)

a = apple.pop(0)
b = apple.pop(-1)
c = str(len(apple))
d = a + c + b
print(d)