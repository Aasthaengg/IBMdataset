import collections

n = int(input())
a = list(map(int,input().split()))
a.sort()
s = set(a)

ac = collections.Counter(a)
ans = 0

for i in s:
    if ac[i] < i:
        ans += ac[i]
    else:
        ans += ac[i] - i

print(ans)