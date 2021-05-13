s = input()

if s[-1] != 's':
    s = s + 's'

elif s[-1] == 's':
    s = s + 'es'

print(s)