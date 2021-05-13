N = int(input())
s = input()
ans = 0
for i in range(N):
    left = s[:i]
    right = s[i:]
    both = set(left)&set(right)
    ans = max(ans, len(both))
print(ans)