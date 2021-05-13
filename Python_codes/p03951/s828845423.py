n = int(input())
s = list(input())
t = list(input())
ans = 0
for i in range(n+1):
    if s[len(s)-i:] == t[:i]:
        ans = i
print(2*n-ans)