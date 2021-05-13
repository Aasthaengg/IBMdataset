X = int(input())

n = 1
nX = [X]
k = 360
mk = [360]

while True:
    if mk.count(nX[-1]) == 1:
        print(n)
        break
    n += 1
    mk.append(n * k)
    nX.append(n * X)