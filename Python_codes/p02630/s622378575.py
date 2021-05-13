n = int(input())
a = list(map(int, input().split()))
cnt = [0] * (10 ** 5 + 1)

sum = 0
for i in a:
    cnt[i] += 1
    sum += i

q = int(input())
ans = [0] * q
for _ in range(q):
    b, c = map(int, input().split())
    sum += (c - b) * cnt[b]
    cnt[c] += cnt[b]
    cnt[b] = 0
    ans[_] = sum

print(*ans, sep="\n")