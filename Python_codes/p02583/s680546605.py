N = int(input())
L = list(map(int, input().split()))

count = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x = max(L[i], L[j], L[k])
            y = L[i] + L[j] + L[k]
            if x < y - x and (L[i] != L[j] and L[i] != L[k] and L[j] != L[k]):
                count += 1

print(count)
