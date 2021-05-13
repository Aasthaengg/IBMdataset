# 175 B
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0

for i in range(0, len(L)):
    for j in range(i+1, len(L)):
        for k in range(j+1, len(L)):
            if L[i] != L[j] and L[j] != L[k] and (L[k] < L[i] + L[j]):
                ans += 1
print(ans)