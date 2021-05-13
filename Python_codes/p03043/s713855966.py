import math
a = [int(s) for s in input().split()]
saikoro = a[0]
tensu = a[1]
ans = float(0)

for i in range(1, saikoro+1):
    if i >= tensu:
        ans += 1
    else:
        temp = tensu / i
        temp2 = math.ceil(math.log(temp, 2))
        ans += (1 / int((2 ** temp2)))

print(ans / saikoro)