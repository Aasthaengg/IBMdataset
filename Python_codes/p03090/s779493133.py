n = int(input())
an = []
if n % 2 == 0:
    a = 1
else:
    a = 0

for i in range(n,0,-1):
    for j in range(1, i):
        if j != a:
            an.append([i,j])
    a += 1
print(len(an))
for i in an:
    print(i[0], i[1])