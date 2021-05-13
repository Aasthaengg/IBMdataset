# 解説AC
A = list(input())
cnt = [0] * 26
for s in A:
    cnt[ord(s) - ord("a")] += 1

ans = len(A) * (len(A) - 1) // 2
ans -= sum(c * (c - 1) // 2 for c in cnt)
ans += 1

print(ans)