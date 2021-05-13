s = input()
t = input()
total = 0
for n in range(len(s)):
    if s[n] is not t[n]:
        total = total + 1
print(total)