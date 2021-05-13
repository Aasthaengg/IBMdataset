a1 = [input().split()]
m = int(a1[0][0])
n = int(a1[0][1])
a2 = [input().split() for i in range(m)]
a3 = [input().split() for i in range(n)]
i = 0
while i < m:
    sum = 0
    j = 0
    while j < n:
        s = int(a2[i][j]) * int(a3[j][0])
        sum += s
        j += 1
    print(sum)
    i += 1