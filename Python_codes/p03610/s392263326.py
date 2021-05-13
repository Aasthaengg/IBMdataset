s = input()
x = s[0]
for i in range(len(s)):
    if i % 2 == 0:
        x= x + s[i]
print(x[1:])