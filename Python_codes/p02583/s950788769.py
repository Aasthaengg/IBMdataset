N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0

for i in range(N):
    for j in range(i):
        for k in range(j):
            if L[i] != L[j] and L[j] != L[k]:
                if L[j] + L[k] > L[i]:
                    ans += 1

print(ans)