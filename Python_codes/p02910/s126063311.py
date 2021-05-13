s = input()
print('Yes' if set(s[::2]) <= {'R', 'U', 'D'} and set(s[1::2]) <= {'L', 'U', 'D'} else 'No')