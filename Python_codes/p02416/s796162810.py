a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)

for i in range(len(a)):
    b = list(str(a[i]))
    sum = 0
    for j in b:
        sum += int(j)
    print(sum)