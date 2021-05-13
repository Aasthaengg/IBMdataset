n = int(input())
s = list(input().split())
cnt = 0
for c in ("P", "W", "G", "Y"):
    if s.count(c):
        cnt += 1
ans = "Three" if cnt == 3 else "Four"
print(ans)
