import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
N,M = map(int,input().split())
S = input()
T = input()

L = lcm(N,M)
H = (L/N)*(L/M)
n = int(L/H)
for i in range(n):
  if S[i*int(L/M)] != T[i*int(L/N)]:
    print(-1)
    exit()
print(L)
