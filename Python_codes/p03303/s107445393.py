s = input()
w = int(input())
n = len(s)
ans = ""
i = 0
while i < n:
    ans += s[i]
    i += w
print(ans)