n, k = map(int, input().split())
a = [int(ai) - 1 for ai in input().split()]
s = [0]
cur = 0
for ai in a:
    cur += ai
    cur %= k
    s.append(cur)

d = {}
ans = 0

# first interval
for si in s[:k]:
     if si in d:
         d[si] += 1
     else:
        d[si] = 1
for key in d:
    val = d[key]
    if val > 1:
        ans +=  val * (val - 1) // 2

# syakutori
r = 0
for l in range(k, n+1):
    d[s[r]] -= 1
    if s[l] in d:
        ans += d[s[l]]
        d[s[l]] += 1
    else:
        d[s[l]] = 1
    r += 1

print(ans)
