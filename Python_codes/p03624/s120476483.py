s = list(input())
s = list(set(s))
s.sort()
if len(s) == 26:
    print("None")
l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(26):
    if len(s) <= i:
        print(l[i])
        break
    if s[i] != l[i]:
        print(l[i])
        break
