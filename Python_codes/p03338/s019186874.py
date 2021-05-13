n = int(input())
s = list(input())
ans = 0
for i in range(1, n):
    left = set(s[:i])
    right = set(s[i:])
    seki = left & right
    ans = max(len(seki), ans)
print(ans)