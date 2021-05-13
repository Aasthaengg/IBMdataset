x = int(input())
n = [i**5 for i in range(119+1)]

a = 0
b = 0
res = False
i = 0
while not res:
    sign = 1 - 2*(n[i] < x)
    for j in range(i+1):
        if (n[i] - n[j] * sign) == x:
            print(i,j*sign)
            res = True
    i += 1