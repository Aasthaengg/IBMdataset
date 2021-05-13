s = input()
k = int(input())

dct = []
for i in range(len(s)):
    for j in range(k+1):
        word = s[i:i+j]
        if word not in dct:
            dct.append(word)
dct.sort()

print(dct[k])