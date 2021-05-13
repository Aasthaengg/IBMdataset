import math

N=int(input())
S=list(map(int,input().split()))
F=S[0]
for i in range(N-1):
    F=math.gcd(F,S[i+1])

print(F)