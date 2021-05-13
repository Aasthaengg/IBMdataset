s = input()
p = int(s)

x = 1

numbers = []

while (x <= p):
    x *= 2
    numbers.append(x)

if p == 1:
    answer = 1
else:
    y = numbers.pop()
    answer = numbers.pop()

print(answer)


