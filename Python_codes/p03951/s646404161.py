n = int(input())
s = list(str(input()))
t = list(str(input()))
ans = 0

for i in range(n+1):
    if s[len(s) - i:] == t[:i]:
        ans = i


print(n*2 - ans)