n = int(input())
datA = []
datB = []
buf = []
for i in range(n):
    a,b = map(int, input().split())
    datA.append(a)
    datB.append(b)
    buf.append([a+b,i])
buf.sort(reverse=True)
resA, resB = 0, 0
for i in range(n):
    if i%2 == 0:
        resA += datA[buf[i][1]]
    else:
        resB += datB[buf[i][1]]

print(resA - resB)
