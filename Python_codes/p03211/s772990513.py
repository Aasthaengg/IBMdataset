s = input()
p = 999

for i in range(len(s) - 2 ):
    j = s[i:i+3]
    j = int(j)
    if p > abs(753 - j):
        p = abs(753 - j)

print(p)