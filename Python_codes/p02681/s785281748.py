s = input()
t = input()
print('Yes' if s == t[:-1] and len(s) == len(t) - 1 else 'No')