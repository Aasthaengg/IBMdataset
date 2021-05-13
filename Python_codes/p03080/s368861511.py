N = int(input())
s = input()

r = 0
for c in s:
    if c == 'R':
        r += 1

if r > (N - r):
    print('Yes')
else:
    print('No')
