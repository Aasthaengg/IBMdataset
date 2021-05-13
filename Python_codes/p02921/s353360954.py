s = input()
t = input()
print(len([a == b for a, b in zip(s, t) if a == b]))