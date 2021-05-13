
s = input()
w = int(input())
c = ""

for i in range(len(s)):
    if i % w == 0:
        c += s[i]
print(c)
