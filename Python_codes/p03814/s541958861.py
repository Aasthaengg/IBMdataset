s = input()

a_i = s.index('A')
s1 = s[::-1]
z_i = s1.index('Z')

print((len(s)-z_i)-a_i)