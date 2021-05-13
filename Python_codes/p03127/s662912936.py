from fractions import gcd

n = int(input())
lis = list(map(int, input().split()))

tmp = gcd(lis[0], lis[1])

for i in range(1, n-1):
    tmp = gcd(tmp,lis[i+1])
    
print(tmp)
