s = input()
t = input()

ans = len(s)

for i in range(len(s) - len(t) + 1):
    sub = s[i:i+len(t)]
    ans = min(ans, len(t) - sum(a == b for a, b in zip(sub, t)))

print(ans)