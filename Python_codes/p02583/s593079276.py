N = input()
L = list(map(int, input().split()))

ans = 0
for i in range(len(L)-2):
    for j in range(i+1, len(L)-1):
        for k in range(j+1, len(L)):
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                continue
            elif L[i] + L[j] <= L[k] or L[j] + L[k] <= L[i] or L[k] + L[i] <= L[j]:
                continue
            else:
                ans += 1
print(ans)
