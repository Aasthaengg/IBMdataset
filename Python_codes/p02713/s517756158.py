from math import gcd
k = int(input())

s = 0
#for a in range(1,k+1):
#    for b in range(1,k+1):
#        for c in range(1,k+1):
#            s += gcd(a,gcd(b,c))

# 全部同じのケース
for i in range(1,k+1):
    s += gcd(i,gcd(i,i))

# １つ違うケース
for i in range(1,k+1):
    for j in range(1,k+1):
        if i != j:
            s += gcd(i,gcd(i,j))*3

# 全部違うケース
for a in range(1,k-1):
    for b in range(a+1,k):
        for c in range(b+1,k+1):
            s += gcd(a,gcd(b,c))*6
            
print(s)
