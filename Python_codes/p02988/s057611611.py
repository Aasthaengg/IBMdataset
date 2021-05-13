n = int(input())
s = list(map(int, input().split()))
cnt = 0
for i in range(1, n - 1):
    if s[i] < s[i + 1] and s[i - 1] <= s[i]:
        cnt += 1
    elif s[i] < s[i - 1] and s[i + 1] <= s[i]:
        cnt += 1
print(cnt)
