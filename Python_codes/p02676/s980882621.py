from sys import stdin
data = stdin.readlines()

k = int(data[0].split()[0])
s = data[1].split()[0]

if len(s) <= k:
    print(s)
else:
    print(s[0:k] + "...")