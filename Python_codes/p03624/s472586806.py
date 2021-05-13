s = input()
alphabet = list(chr(ord("a")+i)for i in range(26))
a = [0]*26

for i in s:
    for j in range(26):
        if i == alphabet[j]:
            a[j] = 1

b = []
for i in range(26):
    if a[i] == 0:
        b.append(alphabet[i])

if len(b) != 0:
    print(b[0])
else:
    print("None")
