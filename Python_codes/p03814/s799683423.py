s = input()

a = s.index('A')
z = [i for i, x in enumerate(s) if x == 'Z']
print(max(z)+1-a)
