from sys import stdin
import fractions
n,k = [int(x) for x in stdin.readline().rstrip().split()]
li = list(map(int,stdin.readline().rstrip().split()))
li.sort()
if k > li[-1]:
    print("IMPOSSIBLE")
    exit()
gcd = li[0] 
for i in range(n-1):
    gcd = fractions.gcd(gcd,li[i+1])
if k%gcd != 0:
    print("IMPOSSIBLE")
    exit()
print("POSSIBLE")