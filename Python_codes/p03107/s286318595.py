S = input()
c0 = 0
c1 = 0
for s in S:
    if s == "0":
        c0 += 1
    else:
        c1 += 1

print(2*min(c0, c1))