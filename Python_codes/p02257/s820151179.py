import math

ans = 0
N = int(input())
for i in range(N):
    a = int(input())
    if a != 2 and a%2 == 0:
        continue
    b = True
    for j in range(3, int(math.sqrt(a))+1, 2):
        if a%j == 0:
            b = False
    if b:
        ans += 1

print(ans)