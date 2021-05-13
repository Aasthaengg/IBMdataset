s = input()

s = "".join([c for c, i in zip(s, range(len(s))) if i % 2 == 0])

print(s)