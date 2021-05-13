s = input()
t = input()

S = ''.join(sorted(s))
T = ''.join(sorted(t, reverse = True))

if S < T:
    print('Yes')
else:
    print('No')