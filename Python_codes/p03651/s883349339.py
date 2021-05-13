n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
import fractions
num = a[0]
for i in range(1, n):
    num = fractions.gcd(num, a[i])

if k > a[-1]:
    print("IMPOSSIBLE")
elif (k in a) or (k%num==0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")