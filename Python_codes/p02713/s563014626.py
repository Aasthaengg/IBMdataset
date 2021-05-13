import math
n = int(input())+1
sum0 = 0
for i in range(1,n):
    for j in range(1,n):
        a=math.gcd(i,j)
        for k in range(1,n):
            sum0 += math.gcd(a,k)
print(sum0)
