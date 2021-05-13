from collections import defaultdict

N, K = map(int, input().split())
Items = [tuple(map(int, input().split())) for _ in range(N)]
Items.sort(reverse=True, key=lambda x: x[1])
Kinds = defaultdict(int)
ans = 0
k = 0
Candidates = []
for i, (t, d) in enumerate(Items):
    if i < K:
        ans += d
        if t not in Kinds:
            k += 1
        else:
            Candidates.append(d)
        Kinds[t] += 1
        if i == K - 1:
            ans += k ** 2
            a = ans
    else:
        if Kinds[t]:
            continue
        if not Candidates:
            break
        else:
            x = Candidates.pop()
            a -= x
            a -= k ** 2
            k += 1
            a += d
            a += k ** 2
            Kinds[t] -= 1
            ans = max(ans, a)
print(ans)