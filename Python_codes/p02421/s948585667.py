n = int(raw_input())
t = 0
h = 0
for i in range(n):
    line = raw_input().split()
    if line[0] == line[1]:
        t += 1
        h += 1
    elif line[0] > line[1]:
        t += 3
    else:
        h += 3
print '{0} {1}'.format(t,h)