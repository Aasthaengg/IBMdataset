k, x = map(int, input().split())
a = []
for i in range(x-(k-1), x+(k-1+1)):
    a.append(i)
for i in range(len(a)):
    print(str(a[i]) + ' ', end = "")