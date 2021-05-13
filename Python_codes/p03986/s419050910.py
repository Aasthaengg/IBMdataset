X = list(input())
nt, ns = 0, 0
for x in X:
    if x == 'S':
        ns += 1
    elif ns > 0:
        ns -= 1
    else:
        nt += 1
print(nt+ns)
