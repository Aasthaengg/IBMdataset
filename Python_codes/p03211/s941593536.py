s = input()
d = 999
for i in range(len(s) - 2):
    n = int(s[i: i + 3])
    d = min(d, abs(n - 753))
print(d)
