N = int(input())
L = sorted([int(i) for i in input().split()], reverse=True)
# print(L)
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if L[i] < L[j]+L[k] and L[i] != L[j] != L[k]:
                ans += 1
print(ans)
