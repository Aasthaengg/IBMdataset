n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (n+1)
for i in range(n):
    cnt[a[i]] += 1
cntl = sorted(cnt)
print(sum(cntl[:-k]))