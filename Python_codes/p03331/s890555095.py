import math
n = int(input())
if math.log10(n) %1 == 0:
    print(10)
    exit()
else:
    ans = 0
    n = str(n)
    for i in range(len(n)):
        ans += int(n[i])
print(ans)