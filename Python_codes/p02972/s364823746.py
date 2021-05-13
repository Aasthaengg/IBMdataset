n = int(input())
alist = list(map(int, input().split()))
boxList = [0] * (n + 1)

m = 0
resultList = []

for i in range(1, n+1)[::-1]:
    sums = 0
    for j in range(1, n // i):
        sums += boxList[(j+1) * i]
    if sums % 2 != alist[i - 1]:
        boxList[i] = 1
        m+= 1
        resultList.append(i)

print(m)
if m != 0:
    print(' '.join(map(str, resultList)))
