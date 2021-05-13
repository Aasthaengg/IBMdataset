import math
A,B,C,D = map(int,input().split())

E = C*D // math.gcd(C,D)

i = B//C
j = B//D
k = (A-1)//C
l = (A-1)//E
n = (A-1)//D
m = B//E

res = B-(A-1)-(i-k)-(j-n)+(m-l)
print(res)