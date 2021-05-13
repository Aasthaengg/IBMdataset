s = input()

a = s.index('A')
z = list(reversed(s)).index('Z')

print(len(s)-z-a)