N = int(input())
a = list(map(int, input().split()))

ans = 0
i = 0
while i < N:
    j = i + 1
    while j < N:
        if a[j] != a[i]:
            break
        j += 1
    ans += (j - i) // 2
    i = j
print(ans)