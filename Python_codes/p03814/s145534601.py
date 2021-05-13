s = input()

a = s.find('A')
#print(a)
z = 0
for i in range(len(s)):
  if s[i] == 'Z':
    z = i
#print(z)
print(z-a+1)