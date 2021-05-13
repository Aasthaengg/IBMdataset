N, T = map(int, input().split())
a = list(map(int, input().split()))
if N == 1:
    print(1)
    exit()

ans = []
ans.append(a[1] - a[0])
mina = min(a[1], a[0])
maxri = ans[0]
for i in range(2, N):
    ans.append(a[i] - mina)
    maxri = max(ans[i - 1], maxri)
    mina = min(a[i], mina)

print(ans.count(maxri))