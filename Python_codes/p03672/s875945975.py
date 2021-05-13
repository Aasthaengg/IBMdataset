s = input()
if len(s) % 2 == 1:
    s += "."

for i in range(2, len(s), 2):
    if (s[:(len(s)-i)//2]*2 == s[:len(s)-i]):
        print(len(s)-i)
        break