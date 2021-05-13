s = input()
key = "keyence"
j = 0
while j < len(key) and s[j] == key[j]:
    j += 1

j -= 1
for i in range(len(key) - j - 1):
    if s[len(s) - 1 - i] != key[len(key) - 1 - i]:
        print("NO")
        exit()
print("YES")