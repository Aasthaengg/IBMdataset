import fractions

N = int(input())
a = list(map(int,input().split()))

ans = a[0]
for i in range(1, N):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
ans=ans-1
b=0

for i in a:
    b=b+ans%i
print(b)