import collections
n = int(input())

a = list(map(int,input().split()))

b = collections.Counter(a)

ans = 0

for k,v in b.items():
    if v < k:
        ans += v
    else:
        ans += (v-k)

print(ans)    