n = int(input())
la = [int(w) for w in input().split()]
lb = [int(w) for w in input().split()]

ans = 0

for i in range(n):
    m = min(la[i], lb[i])
    la[i] -= m
    lb[i] -= m
    ans += m

    m = min(la[i + 1], lb[i])
    la[i+1] -= m
    lb[i] -= m
    ans += m

print(ans)
