s = input()
s = [i for i in s]
s.sort()
print('Yes' if ''.join(s) == 'abc' else 'No')