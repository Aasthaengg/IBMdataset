import math
n = int(input())
ans = math.ceil(((1+8*n)**0.5 - 1 )/ 2)
total = ans * (1+ans) // 2
sub = total - n

for i in range(1,ans+1):
    if sub == i:
        continue
    print(i)
