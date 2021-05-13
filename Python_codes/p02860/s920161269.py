input()
s = input(); l = len(s)
if l % 2:
    print('No')
else:
    print('Yes' if (s[:(l//2)] == s[l//2:]) else  'No')