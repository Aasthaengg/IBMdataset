N = int(input())
L = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k] and L[i] + L[k] > L[j] and L[j] + L[k] > L[i]:
                ans += 1
print(ans)
