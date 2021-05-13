import fractions 
n = int(input())
H = list(map(int,input().split()))
num = fractions.gcd(H[0],H[1])
for i in range(2,n-2):
  num = fractions.gcd(num,H[i])
print(num)