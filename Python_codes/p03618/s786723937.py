s = input()

dist = -1
for i in range(26):
    temp = s.count(chr(ord("a")+i))
    dist += temp * ~-temp // 2

print(len(s) * ~-len(s) // 2 - dist)