n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = sorted(a,reverse = True)
max1 = b[0]
max2 = b[1]
for i in a:
    print(max2 if i == max1 else max1)
