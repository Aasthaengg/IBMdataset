s = input()
w = int(input())
ans = ""
for i in range((len(s) // w) + 1):
    if i * w < len(s):
        ans += s[i * w]
print(ans)