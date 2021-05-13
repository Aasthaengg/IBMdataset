import math

l = [int(input()) for _ in range(5)]
m = [math.ceil(l[i]/10)*10 for i in range(5)]
s = sum(m)
ans = [s-m[i]+l[i] for i in range(5)]
print(min(ans))