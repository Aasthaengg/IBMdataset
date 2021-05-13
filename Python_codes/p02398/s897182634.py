x = input()
x = x.split(" ")
x = [int(z) for z in x]
count = 0
for c in range(x[0],x[1]+1):
    if x[2] % c == 0: count += 1
print("%d" % count)