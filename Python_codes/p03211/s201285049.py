s = input()
l = len(s)
d = 1000
for i in range(l):
    tmp = abs(int(s[i:i+3]) - 753)
    if tmp < d:
        d = tmp

print(d)