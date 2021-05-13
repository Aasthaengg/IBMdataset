# ABC172 Making Triangle
N = int(input())
L = list(map(int,input().split()))
d = {i:L.count(i) for i in L}

L = sorted(L)
ans = 0
cnt = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            cnt += 1
            if L[k] < L[i] + L[j] and L[k] != L[i] and L[i] != L[j] and L[j] != L[k]:
                ans += 1
print(ans)