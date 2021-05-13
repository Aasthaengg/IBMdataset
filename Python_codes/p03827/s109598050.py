_ = int(input())
s = input()

ans = 0
n = 0
for c in s:
    n = n + 1 if c == "I" else n - 1
    ans = max(n, ans)

print(ans)
