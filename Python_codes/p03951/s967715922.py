n = int(input())
s = input()
t = input()

lt = min(len(s), len(t))
i = -1
overlap = 0
for i in range(lt):
    if s[-(i + 1):] == t[:i + 1]:
        overlap = i + 1
        if lt >= 2 and s[-(i + 2):] != t[:i + 2]:
            break
    
ans = max(n, len(s) + len(t) - overlap)
print(ans)