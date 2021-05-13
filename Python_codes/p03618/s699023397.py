a = input()
cnt = [0 for _ in range(26)]
for x in a:
    cnt[ord(x) - ord('a')] += 1
ans = len(a) * (len(a)-1) // 2 + 1
for c in cnt:
    ans -= c * (c-1) // 2
print(ans)