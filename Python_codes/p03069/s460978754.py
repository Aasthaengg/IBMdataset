n = int(input())
s = input()

white = s.count('.')
black = n - white
w = 0
b = 0
y = [white]
for i in range(n):
    if s[i] == '#':
        b += 1
    else: w += 1
    y.append(b+white-w)
    if w == white:
        break
print(min(y))