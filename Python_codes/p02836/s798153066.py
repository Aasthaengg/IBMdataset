s = input()
reverse = s[::-1]

result = 0
while s != reverse:
    for i, c in enumerate(s):
        if c != reverse[i]:
            s = s[:i] + reverse[i] + s[i + 1:]
            reverse = s[::-1]
            result += 1
            break
print(result)
