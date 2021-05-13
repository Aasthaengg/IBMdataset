N = int(input())
P = list(map(int, input().split()))

m = N
ans = 0

for i in P:
    if m >= i:
        ans = ans + 1
        m = i
print(ans)