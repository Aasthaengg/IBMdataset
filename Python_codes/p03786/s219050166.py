from collections import Counter

n = int(input())
aaa = list(map(int, input().split()))
cnt = Counter(aaa)
aaa_unique = list(set(aaa))
aaa_unique.sort(reverse=True)

rs = sum(aaa)

ans = 0
for a in aaa_unique:
    rs -= a * cnt[a]
    ans += cnt[a]
    if a > 2 * rs:
        break
print(ans)
