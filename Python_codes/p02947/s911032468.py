n = int(input())
s = [list(input()) for _ in range(n)]
ans = 0
sd = dict([])

for i in s:
    key = ''.join(sorted(i))
    sd.setdefault(key, 0)
    sd[key] += 1
    
for v in sd.values():
    ans += v * (v - 1) // 2
print(ans)