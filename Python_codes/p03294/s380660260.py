from fractions import gcd
n = int(input())
l = list(map(int,input().split()))
lcm = 1
for i in range(n):
    lcm = lcm*l[i]//gcd(l[i],lcm)
x = lcm-1
print(sum([x%i for i in l]))