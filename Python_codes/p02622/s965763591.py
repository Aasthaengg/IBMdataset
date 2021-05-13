s = input()
t = input()

ans = abs(len(s) - len(t))
count = min(len(s), len(t))

for i in range(count):
    if s[i] != t [i]:
        ans += 1
print(ans)