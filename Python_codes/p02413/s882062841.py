r,c = [int(i) for i in input().split()]

a = [[0 for i in range(c)]for j in range(r)]


for s in range(r):
    a[s] = [int(x) for x in input().split()]

for t in range(r):
    a_sum = sum(a[t])
    a[t].append(a_sum)

lastline = [0 for i in range(c+1)]
for t in range(r):
    for s in range(c+1):
        lastline[s] += a[t][s]
a.append(lastline)

for i in a:
    output = [str(j) for j in i]
    print(' '.join(output))