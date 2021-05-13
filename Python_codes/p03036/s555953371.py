r, d, x = map(int, input().split())
first = r*x - d
ls = [first]
for i in range(9):
    tmp = (ls[len(ls) - 1]) * r - d
    ls.append(tmp)

for i in ls:
    print(i)

