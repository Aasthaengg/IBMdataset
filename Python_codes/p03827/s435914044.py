n = int(input())
s = input()
x = 0
y = 0
for i in range(n):
    if s[i] == 'I':
        y += 1
    else:
        y -= 1
    if y > x:
        x = y
print(x)