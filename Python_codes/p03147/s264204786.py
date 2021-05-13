N=int(input())
H=[0]+list(map(int,input().split()))
M=max(H)

K=0
for a in range(1,M+1):
    for b in range(N):
        if H[b]<a and H[b+1]>=a:
            K+=1
print(K)