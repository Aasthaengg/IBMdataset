s = input()

w = ''
n = len(s)
for a in range(0, n):
    if a % 2 == 0:
        w += s[a]

print(w)
