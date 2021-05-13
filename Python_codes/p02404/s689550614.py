b = []
c = []
d = []
while True:
    a = input().split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    if a[0] == 0 and a[1] == 0:
        break
    else:
        b.append("#"*a[1])
        d.append("#"+("."*(a[1]-2))+"#")
        c.append(a[0])
for i in range(len(c)):
    print(b[i])
    for j in range(c[i]-2):
        print(d[i])
    print(b[i])
    print("\n",end="")
