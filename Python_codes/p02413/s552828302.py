i = list(map(lambda x: int(x), input().split(" ")))
count = 0
h = list()
c = [0 for i in range(0, i[1]+1)]
while count < i[0]:
    l = list(map(lambda x: int(x), input().split(" ")))
    l.append(sum(l))
    h.append(l)
    for j, c_ in enumerate(l):
        c[j] += c_
    count += 1
for r_ in h:
    print("%d" % r_[0], end="")
    for c_ in r_[1:]:
        print(" %d" % c_, end="")
    print("")

print("%d" % c[0], end="")
for c_ in c[1:]:
    print(" %d" % c_, end="")
print("")