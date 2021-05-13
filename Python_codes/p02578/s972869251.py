n = int(input())
aaa = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if aaa[i - 1] > aaa[i]:
        ans += aaa[i - 1] - aaa[i]
        aaa[i] = aaa[i - 1]
print(ans)
