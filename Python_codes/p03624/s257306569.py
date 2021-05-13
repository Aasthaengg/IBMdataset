import string

s = input()

t = string.ascii_lowercase

for i in t:
    if i not in s:
        print(i)
        exit()

print("None")
