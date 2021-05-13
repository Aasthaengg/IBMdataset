N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(len(L)):
    for j in range(len(L)):
        for k in range(len(L)):
            if i < j < k:
                if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                    continue
                if L[i] + L[j] + L[k] <= max(L[i], L[j], L[k]) * 2:
                    continue
                ans += 1

print(ans)