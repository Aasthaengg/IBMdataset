def i_input(): return input()


s = i_input()
if s[-1] == 's':
    s = s + 'es'
else:
    s = s + 's'

print(s)
