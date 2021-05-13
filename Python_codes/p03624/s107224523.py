s = set(list(input()))
strings = [chr(i) for i in range(97, 97+26)]

for i in strings:
    if not i in s:
        print(i)
        exit()
print(None)
