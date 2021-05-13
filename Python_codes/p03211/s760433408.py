s = list(str(input()))
b = 999
for i in range(len(s) - 2):
    a = int(s[i] + s[i + 1] + s[i + 2])
    if abs(a - 753) < b:
        b = abs(a - 753)
print(b)