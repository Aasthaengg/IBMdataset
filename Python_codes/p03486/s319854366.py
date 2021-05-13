S = sorted(list(input()))
T = sorted(list(input()), reverse = True)

s = ''
for i in S:
    s += i
t = ''
for i in T:
    t += i

if s < t:
    print('Yes')
else:
    print('No')