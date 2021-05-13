a, b = [x for x in input().split()]

l = []

l.append(''.join([a] * int(b)))
l.append(''.join([b] * int(a)))

l.sort()

print(l[0])
