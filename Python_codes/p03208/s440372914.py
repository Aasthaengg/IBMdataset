N,K = list(map(int,input().split()))
H=[]

for n in range(N):
    H.append(int(input()))
    
H.sort()

ans=10**10
for h in range(K-1,N):
    h_min=H[h-K+1]
    h_max=H[h]
    if ans > h_max-h_min:
        ans=h_max-h_min
print(ans)