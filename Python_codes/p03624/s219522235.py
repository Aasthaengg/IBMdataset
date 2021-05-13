s = input()

a = ord('a')

t = set()
for c in s:
    t.add(ord(c) - a)

for i in range(26):
    if not i in t:
        print(chr(a + i))
        exit()

print("None")
