N = int(input())
L = list(map(int, input().split()))
cnt = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j!=k!=i and L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[k]+L[i]>L[j] and L[i]!=L[j]!=L[k]!=L[i]:
                cnt += 1
print(cnt//6)