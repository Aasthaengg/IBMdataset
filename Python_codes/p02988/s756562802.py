n = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    Pps = sorted(P[i:i + 3])
    if Pps[1] == P[i + 1]:
        ans += 1
print(ans)