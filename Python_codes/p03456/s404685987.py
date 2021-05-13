import math
a, b = map(str, input().split())
ans = int(a+b)
for i in range(ans):
    route = pow(i, 2)
    if ans == route:
        print("Yes")
        exit()
print("No")