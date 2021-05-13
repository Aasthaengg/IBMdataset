A, B, C = map(int, input().split())

l = [A, B, C]

num = str(l.pop(l.index(max(l)))) + str(l.pop(l.index(max(l))))

print(int(num) + max(l))
