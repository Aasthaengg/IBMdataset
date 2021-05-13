
N, K = map(int, input().split())
A = list(map(int, input().split()))
kind = len(set(A))
cnt = [0] * 202020
for a in A:
    cnt[a] += 1
cnt = sorted(filter(lambda x: x > 0, cnt))
ans = 0
for c in cnt:
    if kind <= K:
        break
    ans += c
    kind -= 1
print(ans)