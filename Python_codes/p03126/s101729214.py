n, m = map(int, input().split())
cnt = [0 for i in range(m)]
for i in range(n):
    a = list(map(int, input().split()))[1:]
    for j in a:
        cnt[j - 1] += 1
ans = cnt.count(n)
print(ans)