from fractions import gcd
n = int(input())
monster = list(map(int, input().split()))
a=gcd(monster[0],monster[1])
for i in range(2,n):
    a=gcd(a,monster[i])
print(a)