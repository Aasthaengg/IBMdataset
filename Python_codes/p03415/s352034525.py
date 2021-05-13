k = []
for i in range(3):
    l = list(input())
    k.append(l)
s = ''
for i in range(3):
    s += k[i][i]
print(s)