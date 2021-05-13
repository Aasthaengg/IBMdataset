s = [p for p in input()]
t = [p for p in input()]
s.sort()
t.sort()
t.reverse()
print('Yes' if s < t else 'No')