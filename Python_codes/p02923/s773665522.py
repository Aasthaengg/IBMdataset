N = int(input())
H = list(map(int,input().split()))

stp = [0]*(N+1)
stp[0] = 0

for i in range(1,N):
    if H[i]<=H[i-1]:
        stp[i] = stp[i-1] +1
    else:
        stp[i] = 0
        
print(max(stp))