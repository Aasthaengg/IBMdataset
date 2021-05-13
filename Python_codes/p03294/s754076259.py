n= int(input())
a =list(map(int,input().split()))
ans = a[0]

def gcd(c, b):
    if b == 0:
        return c
    return gcd(b,c%b)

for i in range(n-1):
    ans = ans*a[i+1] // gcd(ans,a[i+1])
sum = 0
for i in range(n):
    sum += (ans-1)%a[i]
print(sum)