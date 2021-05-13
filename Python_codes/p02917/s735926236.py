# AtCoder Beginner Contest 140
# C - Maximal Value

N=int(input())
Bfirst=[10**5+3]
B=list(map(int,input().split()))
Blast=[10**5+3]
BL=Bfirst+B+Blast

ans=0

for i in range (N):
    ans+= min(BL[i],BL[i+1])

print(ans)