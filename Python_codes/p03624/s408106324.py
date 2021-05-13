import string

s = set(sorted(input()))

for i in string.ascii_lowercase:
    if i not in s:
        print(i)
        exit()
print("None")