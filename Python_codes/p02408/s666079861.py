n = input()
a = []
for i in range(n):
    a.append(raw_input().split())
for j in range(1,14):
    if ['S', str(j)] not in a:
        print 'S', str(j)
for j in range(1,14):
    if ['H', str(j)] not in a:
        print 'H', str(j)
for j in range(1,14):
    if ['C', str(j)] not in a:
        print 'C', str(j)
for j in range(1,14):
    if ['D', str(j)] not in a:
        print 'D', str(j)