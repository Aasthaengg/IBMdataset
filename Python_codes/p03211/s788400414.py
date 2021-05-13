s = input()
min_abs = 1000
for i in range(len(s) - 2):
    if abs(753 - int(s[i: i + 3])) < min_abs:
        min_abs = abs(753 - int(s[i: i + 3]))
print(min_abs)