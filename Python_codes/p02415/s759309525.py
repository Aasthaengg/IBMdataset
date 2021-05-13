l = [c.lower() if c.isupper() else c.upper() for c in list(input())]
print(''.join(l))