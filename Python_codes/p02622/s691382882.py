s = input()
t = input()
print(sum(True for x, y in zip(s, t) if x != y))