n = int(input())

ns = set()
for i in range(0, 26):
    for j in range(0, 16):
        ns.add(4*i + 7*j)
if n in ns:
    print('Yes')
else:
    print('No')