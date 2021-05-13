import math
primenum =int(input())
ans = 0
for p in range(primenum):
    targ = int(input())
    for t in range(2,math.floor(math.sqrt(targ)) + 1):
        if targ % t == 0:
            break
    else:
        ans += 1
print(ans)