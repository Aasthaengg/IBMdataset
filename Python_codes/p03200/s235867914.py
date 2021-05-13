s = input()

a = 0
b = s.count('B')
move = 0

for i in reversed(range(len(s))):
    if s[i] == 'B':
        move += (len(s) - a - (i + 1))
        a += 1
print(move)