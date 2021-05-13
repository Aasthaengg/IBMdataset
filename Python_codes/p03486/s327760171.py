s = input()
t = input()
print('Yes' if ''.join(sorted(s)) < ''.join(sorted(t, reverse=True)) else 'No')