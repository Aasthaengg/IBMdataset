p = input()
s = list(p)

number = len(s) - 2
front = s[0]
rear = s.pop()

print(front, end='')
print(number, end='')
print(rear)