n = input()
s = [0] * 13
h = [0] * 13
c = [0] * 13
d = [0] * 13
for i in range(n):
    x = map(str, raw_input().split())
    if x[0] == 'S':
        s[int(x[1]) - 1] = 1
    if x[0] == 'H':
        h[int(x[1]) - 1] = 1
    if x[0] == 'C':
        c[int(x[1]) - 1] = 1
    if x[0] == 'D':
        d[int(x[1]) - 1] = 1
for i in range(13):
    if s[i] == 0:
        print 'S', (i+1)
for i in range(13):
    if h[i] == 0:
        print 'H', (i+1)
for i in range(13):
    if c[i] == 0:
        print 'C', (i+1)
for i in range(13):
    if d[i] == 0:
        print 'D', (i+1)