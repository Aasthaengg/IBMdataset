n = int(input())
d = dict()
for i in range(n):
    s = list(input())
    if s[0] == "M" or s[0] == "A" or s[0] == "R" or s[0] == "C" or s[0] == "H":
        if s[0] not in d:
            d[s[0]] = 1
        else:
            d[s[0]] += 1
count = 0
d = list(d.values())
if len(d) == 3:
    count += d[0] * d[1] * d[2]
elif len(d) == 4:
    count += d[0] * d[1] * d[2]
    count += d[3] * d[1] * d[2]
    count += d[0] * d[1] * d[3]
    count += d[0] * d[3] * d[2]
elif len(d) == 5:    
    count += d[0] * d[1] * d[2]
    count += d[3] * d[1] * d[2]
    count += d[0] * d[1] * d[3]
    count += d[0] * d[3] * d[2]

    # count += d[0] * d[1] * d[2]
    count += d[4] * d[1] * d[2]
    count += d[0] * d[1] * d[4]
    count += d[0] * d[4] * d[2]

    # count += d[4] * d[1] * d[2]
    # count += d[3] * d[1] * d[2]
    count += d[4] * d[1] * d[3]
    count += d[4] * d[3] * d[2]

    # count += d[0] * d[4] * d[2]
    # count += d[3] * d[4] * d[2]
    count += d[0] * d[4] * d[3]
    # count += d[0] * d[3] * d[2]


print(count)