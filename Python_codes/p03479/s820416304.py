import math
x,y = map(int,input().split())

# ans = int(math.log2(y/x) + 1)
ans = 0
now = x
while now <= y:
    ans += 1
    now *= 2


print(ans)
