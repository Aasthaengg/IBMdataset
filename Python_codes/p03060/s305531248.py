N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ANS = 0

for i in range(N):
    if V[i] > C[i]:
        ANS = ANS + (V[i] - C[i])
        
print(ANS)