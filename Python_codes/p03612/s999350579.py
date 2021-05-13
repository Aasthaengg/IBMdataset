n = int(input())
L = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if L[i] == i + 1:
        if i != n - 1:
            L[i + 1] = L[i]
        cnt += 1
print(cnt)
