import sys

inLine = []
strings = []
for line in sys.stdin:
    for i in range(len(list(str(line).lower()))):
        strings.append(list(str(line).lower())[i])
arr = []
for i in range(26):
    arr.append(0)

for i in range(len(strings)):
    if ord(strings[i]) >= 97 and ord(strings[i]) <= 122:
        arr[ord(strings[i]) - 97] += 1

for i in range(97,123):
    print(chr(i) + " : "  + str(arr[i - 97]))

