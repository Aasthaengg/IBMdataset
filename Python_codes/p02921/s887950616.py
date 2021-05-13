s = input()
t = input()

result = len(list([True for c1, c2 in zip(s, t) if c1 == c2]))
print(result)