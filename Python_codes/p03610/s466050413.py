s = input()

a = len(s)
b =""

if a % 2 == 0:
    for i in range(0,a-1,2):
        b += s[i]
else:
    for i in range(0,a,2):
        b += s[i]

print(b)
