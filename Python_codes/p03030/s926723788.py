n = int(input())
l = []
for i in range(n):
    sp = input().split()
    l.append((sp[0], int(sp[1]), i+1))

a = sorted(l, key=lambda i: i[1], reverse=True)
a = sorted(a, key=lambda i: i[0])

for i in range(n):
    print(a[i][2])