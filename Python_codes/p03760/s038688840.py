s1 = input()
s2 = input()
s = [ 'a' for _ in range(len(s1) + len(s2))]

s[::2] = s1
s[1::2] = s2

print(''.join(s))
