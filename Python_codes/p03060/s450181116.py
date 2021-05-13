N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

W = [V[i]-C[i] for i in range(0,N,1)]

ans =0

for i in range(0,N,1):
    if W[i]>0:
        ans += W[i]
print(ans)