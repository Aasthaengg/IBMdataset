n = int(input())
vn = list(map(int, input().split()))
cn = list(map(int, input().split()))
ans = 0

for i in range(n):
    if vn[i] - cn[i] > 0:
        ans += vn[i] - cn[i]

print(ans)