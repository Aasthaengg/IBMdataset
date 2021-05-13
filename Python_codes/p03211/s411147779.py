s = input()
m = 1000
for i in range(len(s)):
    x = int(s[i:i+3])
    if m > abs(753-x):
        m = abs(753-x)
print(m)