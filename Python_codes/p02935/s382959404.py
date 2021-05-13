N = int(input())
V = sorted(map(int,input().split()))
potvalue = V[0]
for i in range(1,N):
    potvalue = (potvalue + V[i])/2
    
print(potvalue)