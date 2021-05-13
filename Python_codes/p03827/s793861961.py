n = int(input())
S = input()
now = 0
ans = 0
for s in S:
    if s == "I":
        now = now + 1
    else:
        now = now - 1
    ans = max(now, ans)

print(ans)