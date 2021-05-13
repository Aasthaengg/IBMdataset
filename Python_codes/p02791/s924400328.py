N = int(input())
P = list(map(int,input().split()))

ans = 0
n = P[0]

for i in P:
    if n >= i:
        ans += 1
        n = i

print(ans)