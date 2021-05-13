
N = int(input())

Vn = list(map(int, input().split()))
Cn = list(map(int, input().split()))

ans = 0
for i in range(N):
    difference = Vn[i] - Cn[i]
    if difference > 0:
        ans += difference

print(ans)