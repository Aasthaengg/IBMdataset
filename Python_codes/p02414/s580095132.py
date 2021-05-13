n,m,l = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for j in range(m):
    b.append(list(map(int, input().split())))
for  k in range(n):
    for o in range(l):
        sum = 0
        for p in range(m):
            sum += (a[k][p] * b[p][o])
        print(sum, end = "")
        if o != l-1:
            print(" ", end = "")
    print()
