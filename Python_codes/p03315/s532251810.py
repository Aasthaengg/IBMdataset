s = str(input())
n = 0
for i in range(4):
    if s[i] == '+':
        n += 1
    elif s[i] == '-':
        n -= 1
print(n)