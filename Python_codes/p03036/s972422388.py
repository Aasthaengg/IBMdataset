r, d, xs = map(int, input().split())
li = []
xi = 0
for i in range(10):
    xi = r*xs-d
    li.append(xi)
    xs = xi

for i in li:
    print(i)