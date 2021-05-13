n = list(map(int, input().split()))
a =[]
c = 1
b = []

for i in range(1, n[0]+1):
    b.append(i)

for j in range(1, n[1]+1):
    a.append(j)

for k in range(b[-1]):
    if b[-1] == a[-1]:
        print(c)
        break
    else:
        a[-1] += 1
        c += 1