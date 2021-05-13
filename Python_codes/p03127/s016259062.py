import fractions
n = int(input())
li = list(map(int,input().split()))
gcd1 = 0
gcd1 = fractions.gcd(li[0],li[1])
for i in range(2,n):
    gcd1 = fractions.gcd(gcd1,li[i])
print(gcd1)