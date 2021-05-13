c = [int(x) for x in input().split()]
c.append(sum(c))
for i in c:
    if i % 3 == 0:
        print("Possible")
        break
else:
    print("Impossible")