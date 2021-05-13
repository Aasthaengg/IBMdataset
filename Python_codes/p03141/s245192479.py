N, *AB = map(int, open(0).read().split())
AB = [(a, b) for a, b in zip(*[iter(AB)] * 2)]
AB.sort(key=lambda x: x[0] + x[1], reverse=True)
ans = sum(a for a, _ in AB)
for a, b in AB[1::2]:
    ans -= a + b
print(ans)
