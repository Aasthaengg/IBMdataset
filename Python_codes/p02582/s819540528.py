s = input()
t = s.count('R')
if t == 2:
    if s[1] == 'R':
        print(2)
    else:
        print(1)
else:
    print(t)