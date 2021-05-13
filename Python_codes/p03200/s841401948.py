s = input()
a = 0; b = 0
for i in range(len(s)):
    if s[i] == "W":
        a += i
        b += 1
print(a-b*(b-1)//2)