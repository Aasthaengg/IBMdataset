from collections import defaultdict
d = defaultdict(int)

n = int(input())
a = list(map(int,input().split()))

for ai in a:
    d[ai] += 1

ans = 0
for k,v in d.items():
    if(k > v):
        ans += v
    else:
        ans += (v-k)

print(ans)