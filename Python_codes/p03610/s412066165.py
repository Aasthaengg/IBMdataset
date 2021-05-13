s = list(input())
output = []
for i in range(len(s)):
    if i % 2 == 0:
        output.append(s[i])
    else:
        pass
print("".join(output))