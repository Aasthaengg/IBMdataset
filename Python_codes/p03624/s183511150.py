import string
S = set(input())
for c in string.ascii_lowercase:
    if c not in S:
        print(c)
        break
else:
    print('None')