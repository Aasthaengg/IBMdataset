import collections
s = input()

c = collections.Counter(s)

for ch in c:
    if c[ch] >= 2:
        print("no")
        break
else:
    print("yes")
