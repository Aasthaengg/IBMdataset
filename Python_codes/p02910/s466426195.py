s = input()
odd = ["R","U","D"]
even = ["L","U","D"]

for i in range(len(s))[0::2]:
    if not s[i] in odd:
        print('No')
        exit(0)

for i in range(len(s))[1::2]:
    if not s[i] in even:
        print('No')
        exit(0)

print('Yes')