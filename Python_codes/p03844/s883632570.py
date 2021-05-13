s = input().split()

a = int(s[0])
b = int(s[2])

if s[1] == '+':
    print(a + b)
else:
    print(a - b)