n = int(input())
a = list(map(int,input().split()))

d = {}
ans = 0

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for k,v in d.items():
    if k <= v:
        ans += v-k
    else:
        ans += v

print(ans)
