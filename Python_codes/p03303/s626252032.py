s = list(input())
w = int(input())
ans = ''
for i in range(len(s)):
    if i==0 or i%w==0:
        ans += s[i]
print(ans)