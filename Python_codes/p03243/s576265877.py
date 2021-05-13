n = int(input())
for i in range(n,1000):
    a = str(i)
    if a[0] == a[1] and a[0] == a[2]:
        print(i)
        break
