N = input()

s = 0
for d in N:
    s += ord(d) - ord('0')
if s % 9 == 0:
    print('Yes')
else:
    print('No')

