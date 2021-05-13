import math
n = int(input())
a_li = list(map(int,input().split()))
for i in range(n-1):
    a_li[i+1] = math.gcd(a_li[i],a_li[i+1])
print(a_li[i+1])