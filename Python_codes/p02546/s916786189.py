a = input()
b = [x for x in a]

if b[len(b) -1] == 's':
    print(a+'es')
else:
    print(a+'s')