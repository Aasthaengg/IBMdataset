n = int(input())
aaa = [0] + list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    j = aaa[i]
    if aaa[i] == j and aaa[j] == i:
        ans += 1
print(ans // 2)
