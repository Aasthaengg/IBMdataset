N1, N2, N3, N4 = map(int, input().split())
a = list()
a.append(N1)
a.append(N2)
a.append(N3)
a.append(N4)
a.sort()

if a[0] == 1 and a[1] == 4 and a[2] == 7 and a[3] == 9:
    print("YES")
else:
    print("NO")