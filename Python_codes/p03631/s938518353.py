s = input()
s_rev = ''.join(list(reversed(s)))
print('Yes') if s == s_rev else print('No')