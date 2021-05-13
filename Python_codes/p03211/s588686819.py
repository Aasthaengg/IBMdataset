s = input()

d = 1001001

for i in range(len(s) - 1):
    x = int(s[i : i + 3])
    tmp = abs(x - 753)
    if tmp < d:
        d = tmp

print(d)
