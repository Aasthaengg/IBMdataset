x = int(input())
l = set([1])
i = 1
while i < x:
    j = 2
    while j < 10:
        if i**j <= x:
            l.add(i**j)
        j += 1
    i += 1

print(max(l))