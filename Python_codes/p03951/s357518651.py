N = int(input())
s = input()
t = input()

ans = len(s) + len(t)
for i in range(len(s)):
    if t[:i+1] in s:
        ans = min(ans, len(s) + len(t) - (i+1))
        
print(ans)