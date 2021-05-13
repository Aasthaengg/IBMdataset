s = input()
t = input()

s = sorted(list(s))
t = sorted(list(t))[::-1]

print('Yes' if s<t else 'No')