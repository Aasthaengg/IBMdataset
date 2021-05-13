A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

L = [list(map(int, input().split())) for _ in range(M)]

# 割引券を使わない
m = min(a) + min(b)
ans = []
ans.append(m)
for i in range(M):
    x = L[i][0]
    y = L[i][1]
    c = L[i][2]
    p = a[x - 1]
    k = b[y - 1]
    ans.append(p + k - c)

print(min(ans))