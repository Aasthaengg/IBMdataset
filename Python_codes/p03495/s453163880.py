n, k = map(int, input().split())
a = list(map(int, input().split()))
if len(set(a)) == k:
    print(0)
    exit()

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

s = sorted(d.items(), key=lambda x:x[1])
ans = 0
for j in range(len(s) - k):
    ans += s[j][1]

print(ans)