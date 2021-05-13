import fileinput

d = {chr(k) : 0 for k in range(97, 123)}
for line in fileinput.input():
    for c in line.lower():
        if c in d:
            d[c] += 1

for k, v in d.items():
    print("{0} : {1}".format(k, v))

