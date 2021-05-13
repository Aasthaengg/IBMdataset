s=input()
print('Yes' if ('R' not in s[1::2]) and ('L' not in s[::2]) else 'No')