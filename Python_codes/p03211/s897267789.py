s = input()
result = []
for i in range(len(s)-2):
    tmp = int(s[i:i+3])
    result.append(abs(tmp - 753))

print(min(result))