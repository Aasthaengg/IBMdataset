n,k = map(int,input().split())
al = list(map(int,input().split()))

# a,bの最大公約数
def gcd(a, b):
   while b:
       a, b = b, a % b
   return a

tmp = al[0]
for a in al:
    tmp = gcd(a, tmp)

if k % tmp == 0 and max(al) >= k:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")