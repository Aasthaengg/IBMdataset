# 126 A

n, k = map(int, input().split())
s = input()

ans = ""
for i in range(len(s)):
    if i != k-1:
        ans += s[i]
    else:
        ans += s[k-1].lower()

print(ans)